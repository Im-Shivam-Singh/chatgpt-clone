from app.vectordb.factory import VectorStoreFactory


class VectorStoreService:

    def __init__(self):
        self.provider = VectorStoreFactory.get_provider()

    def create_index(self, recreate: bool = False):
        self.provider.create_index(recreate=recreate)

    def upsert(self, docs):
        self.provider.upsert(docs)

    def search(self, query: str, embedding, k):
        return self.provider.search(query, embedding, k)