from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict
import os

load_dotenv()

model = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="openai/gpt-oss-120b",
    temperature=0
)

# Schema
class Review(TypedDict):
    summary: str
    sentiment: str
    key_themes :list[str]
    pros:str
    cons : str

# Structured Output
structured_model = model.with_structured_output(
    Review,
    method="json_schema",
    strict=True
)

result = structured_model.invoke("""Social media has become an essential part of our daily lives. Platforms like Instagram, Facebook, YouTube, and LinkedIn help people connect, communicate, and share information across the world. One of its biggest advantages is that it provides easy access to knowledge, entertainment, business opportunities, and global networking. Students can use social media for learning, while businesses can promote their products and reach millions of customers. However, excessive use of social media can lead to addiction, reduced productivity, cyberbullying, misinformation, and privacy issues. It can also negatively affect mental health by encouraging unhealthy comparisons. Therefore, social media has both positive and negative impacts on society. Its effectiveness depends on how responsibly we use it.

""")

print(result)
print(result["sentiment"])
print(result["summary"])








from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="openai/gpt-oss-120b",
    temperature=0.7
) 

prompt = ChatPromptTemplate(
    template_format= "genenrate 5 interesting fact about {topic}",
    input_vaiables =['topic']
)
llm = model.invoke()
print(os.getenv("GROQ_API_KEY") is not None)


parser = StrOutputParser()

chain = prompt | llm | parser
result=chain.invoke({'topic': 'cricket'})
print(result)
