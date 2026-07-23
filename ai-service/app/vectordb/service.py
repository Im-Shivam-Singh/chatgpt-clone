from app.vectordb.factory import VectorStoreFactory


class VectorStoreService:

    def __init__(self):
        self.provider = VectorStoreFactory.get_provider()

    def upsert(self, docs):
        self.provider.upsert(docs)

    def search(self, embedding, k):
        return self.provider.search(embedding, k)