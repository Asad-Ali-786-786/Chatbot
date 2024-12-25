# from chromadb.config import Settings
# from chromadb import Client

# def store_vectors(data, embeddings):
#     client = Client(Settings())
#     collection = client.get_or_create_collection("chatbot_embeddings")
#     for item, vector in zip(data, embeddings):
#         collection.add(doc=item, embedding=vector)

# def query_vector(query_embedding):
#     client = Client(Settings())
#     collection = client.get_collection("chatbot_embeddings")
#     results = collection.query(embedding=query_embedding, top_k=3)
#     return results



