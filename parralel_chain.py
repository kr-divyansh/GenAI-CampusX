import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
# Load .env file explicitly
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env", override=True)

# Get API key
api_key = os.getenv("GROQ_API_KEY")

print("API KEY LOADED:", api_key is not None)

# Initialize LLM
model1 = ChatGroq(
    api_key=api_key,
    model="openai/gpt-oss-120b",
    temperature=0.7
)
model2 = ChatGroq(
    api_key=api_key,
    model="openai/gpt-oss-120b",
    temperature=0.7
)

prompt1 = ChatPromptTemplate.from_template(
     "generate short and simple notes from the following text \n {topic}"
    
)

prompt2 = ChatPromptTemplate.from_template(
     "create a quiz of 5 question of {topic}"
    
)

prompt3 = ChatPromptTemplate.from_template(
    """
    Merge the provided notes and quiz into a single document.

    NOTES:
    {notes}

    QUIZ:
    {quiz}
    """
)
parser =StrOutputParser()

parallel_runnable =({
    'notes': prompt1 | model1 |parser,
    'quiz' : prompt2 | model2 |parser
})
merge_chain = prompt3 | model1 | parser

chain = parallel_runnable | merge_chain | parser

#chain = prompt1 | model1 | parser | prompt2 | model2 | parser | prompt3 |model1|parser ------->if we use sequential chains
topic ='communism'
# Invoke model
response = chain.invoke({'topic':'communism'}) 
print(response)




