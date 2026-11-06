from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()

documents=[
"delhi is the capital of india",
"mumbai is the financial capital of india",
"KOLKATA is the cultural capital of india",
"CHENNAI is the IT capital of india"

]

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)
embed = embeddings.embed_documents(documents)
print(str(embed))