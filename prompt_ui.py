
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
import streamlit as st

# Load environment variables
load_dotenv()

# Initialize LLM
model = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="openai/gpt-oss-120b",
    temperature=0.7
) 


# Create Streamlit UI
st.title("RESEARCH TOOL")
st.subheader("AI-Powered Dynamic Prompt Generator")

# User inputs
user_input = st.text_area("What do you want to ask?")

# Desired answer length
answer_length = st.selectbox(
    "Select your desired answer length:",
    ["Short", "Medium", "Long"]
)

# Expected answer style
answer_style = st.selectbox(
    "How do you want your answer?",
    [
        "Simple English",
        "Detailed Explanation",
        "Bullet Points",
        "Professional",
        "Beginner Friendly",
        "Exam Oriented",
        "Step-by-Step Explanation"
    ]
)

# Dynamic Prompt Template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an intelligent AI research assistant.

        Answer the user's question according to these instructions:

        Desired Answer Length: {length}

        Expected Answer Style: {style}

        Follow the user's preferences strictly.
        Make your response accurate, clear and relevant.
        """
    ),
    (
        "human",
        "{question}"
    )
])

# Submit button
if st.button("Generate Answer"):

    if user_input.strip():

        with st.spinner("Generating your answer..."):

            # Create dynamic prompt
            chain = prompt | model

            result = chain.invoke({
                "question": user_input,
                "length": answer_length,
                "style": answer_style
            })

            st.subheader("Generated Answer")
            st.write(result.content)

    else:
        st.warning("Please enter your question.")
