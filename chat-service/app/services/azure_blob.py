from datetime import datetime, timedelta, timezone
from uuid import uuid4

from app.settings import get_settings
from azure.core.exceptions import ResourceExistsError
from azure.storage.blob import (
    BlobSasPermissions,
    BlobServiceClient,
    generate_blob_sas,
)


class AzureBlobService:

    settings = get_settings()

    def __init__(self):
        self.client = BlobServiceClient.from_connection_string(
            self.settings.azure_storage_connection_string
        )

        self.container_client = self.client.get_container_client(
            self.settings.azure_storage_container_name
        )

        try:
            self.container_client.create_container()
        except ResourceExistsError:
            pass

    def generate_sas_url(
        self,
        blob_name: str,
        expiry_minutes: int = 60,
    ) -> str:

        sas_token = generate_blob_sas(
            account_name=self.settings.azure_storage_account_name,
            container_name=self.settings.azure_storage_container_name,
            blob_name=blob_name,
            account_key=self.settings.azure_storage_account_key,
            permission=BlobSasPermissions(
                read=True,
            ),
            expiry=datetime.now(timezone.utc)
            + timedelta(minutes=expiry_minutes),
        )

        blob_client = self.container_client.get_blob_client(
            blob_name
        )

        return f"{blob_client.url}?{sas_token}"

    async def upload_file(self, file):

        extension = ""

        if file.filename and "." in file.filename:
            extension = "." + file.filename.rsplit(".", 1)[-1]

        blob_name = f"{uuid4().hex}{extension}"

        blob_client = self.container_client.get_blob_client(
            blob_name
        )

        content = await file.read()

        blob_client.upload_blob(
            content,
            overwrite=False,
        )

        sas_url = self.generate_sas_url(
            blob_name=blob_name,
            expiry_minutes=60,
        )

        return {
            "blob_name": blob_name,
            "filename": file.filename,
            "content_type": file.content_type,
            "url": blob_client.url,
            "sas_url": sas_url,
        }