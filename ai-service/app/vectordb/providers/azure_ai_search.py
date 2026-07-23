from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SimpleField,
    SearchField,
    SearchableField,
    SearchFieldDataType,
    VectorSearch,
    HnswAlgorithmConfiguration,
    VectorSearchProfile,
)
from azure.search.documents.models import VectorizedQuery

from app.settings import get_settings
from app.vectordb.providers.base import BaseVectorStore
from app.vectordb.models import VectorDocument, RetrievedChunk


class AzureAISearchVectorStore(BaseVectorStore):

    def __init__(
        self,
        endpoint: str,
        key: str,
        index_name: str,
    ):
        settings = get_settings()

        self.endpoint = endpoint
        self.index_name = index_name
        self.embedding_dimension = settings.embedding_dimension

        credential = AzureKeyCredential(key)

        self.index_client = SearchIndexClient(
            endpoint=self.endpoint,
            credential=credential,
        )

        self.search_client = SearchClient(
            endpoint=self.endpoint,
            index_name=self.index_name,
            credential=credential,
        )

    def create_index(self):

        indexes = {
            index.name
            for index in self.index_client.list_indexes()
        }

        if self.index_name in indexes:
            print(f"Index '{self.index_name}' already exists.")
            return

        fields = [

            SimpleField(
                name="id",
                type=SearchFieldDataType.String,
                key=True,
            ),

            SimpleField(
                name="document_id",
                type=SearchFieldDataType.String,
                filterable=True,
            ),

            SimpleField(
                name="chunk_index",
                type=SearchFieldDataType.Int32,
                filterable=True,
            ),

            SimpleField(
                name="page",
                type=SearchFieldDataType.Int32,
                filterable=True,
            ),

            SearchableField(
                name="content",
                type=SearchFieldDataType.String,
            ),

            SearchField(
                name="embedding",
                type=SearchFieldDataType.Collection(
                    SearchFieldDataType.Single
                ),
                searchable=True,
                vector_search_dimensions=self.embedding_dimension,
                vector_search_profile_name="default",
            ),

        ]

        vector_search = VectorSearch(

            algorithms=[
                HnswAlgorithmConfiguration(
                    name="hnsw",
                )
            ],

            profiles=[
                VectorSearchProfile(
                    name="default",
                    algorithm_configuration_name="hnsw",
                )
            ],

        )

        index = SearchIndex(
            name=self.index_name,
            fields=fields,
            vector_search=vector_search,
        )

        self.index_client.create_index(index)

        print(f"Created index '{self.index_name}' successfully.")

    def upsert(self, docs: list[VectorDocument]):
        document = [doc.to_dict() for doc in docs]
        result = self.search_client.upload_documents(documents=document)

        for item in result:
            print(item)

    def search(self, embedding, k) -> list[RetrievedChunk]:
        vector_query = VectorizedQuery(
            vector=embedding,
            k_nearest_neighbors=k,
            fields="embedding",
        )
        results: list = self.search_client.search(
            search_text=None,
            vector_queries=[vector_query],
            select=["id", "document_id", "chunk_index", "page", "content"],
        )
        search_results: list[RetrievedChunk] = []
        for item in results:
            retrieved_chunk = RetrievedChunk(
                content=item["content"],
                page=item["page"],
                document_id=item["document_id"],
                score=item["@search.score"]
            )
            search_results.append(retrieved_chunk)
        return search_results