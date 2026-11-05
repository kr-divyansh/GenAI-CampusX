from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
load_dotenv()

documents=[
"delhi is the capital of india",
"mumbai is the financial capital of india",
"KOLKATA is the cultural capital of india",
"CHENNAI is the IT capital of india",
"deep learning is a subset of machine learning",
"deep learning have many applications in computer vision and natural language processing",
"deep learning uses neaurl networs to learn from data",


]
query = "tell me about deep learning"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)
document_embed = embeddings.embed_documents(documents)
print(str(document_embed))
query_embed = embeddings.embed_query(query)
scores = cosine_similarity([query_embed], document_embed)
print(query)
for index in scores.argsort()[0][::-1]:
    print(documents[index])
print("Similarity scores:", scores)