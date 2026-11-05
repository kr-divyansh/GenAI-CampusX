import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load .env file explicitly
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env", override=True)

# Get API key
api_key = os.getenv("GROQ_API_KEY")

print("API KEY LOADED:", api_key is not None)

# Initialize LLM
model = ChatGroq(
    api_key=api_key,
    model="openai/gpt-oss-120b",
    temperature=0.7
)
prompt = ChatPromptTemplate.from_template(
     "genenrate 5 interesting fact about {topic}"
    
)
parser =StrOutputParser()
#chains
chain = prompt | model | parser
# Invoke model
response = chain.invoke({'topic':'bgmi'})
print(response)

