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

prompt1 = ChatPromptTemplate.from_template(
     "detail explanation of the{topic}"
    
)

prompt2 = ChatPromptTemplate.from_template(
     "most imporrtant five points in the {topic}"
    
)
parser =StrOutputParser()
#chains
chain = prompt1 | model | parser | prompt2 | model | parser
# Invoke model
response = chain.invoke({'topic':'bgmi'}) 
print(response)

