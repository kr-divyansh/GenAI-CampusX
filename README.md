# RAG-project-PDF-reader-
first RAG project
# 📚 RAG-Based PDF Question Answering Assistant

An AI-powered PDF Question Answering Assistant built using **Retrieval-Augmented Generation (RAG)**. It allows users to ask questions about PDF documents and receive context-aware answers using document retrieval and a Large Language Model (LLM).

## 🚀 Project Overview

This project combines semantic search with Generative AI to provide answers grounded in information retrieved from PDF documents.

Instead of relying entirely on the LLM's pre-trained knowledge, the system retrieves relevant document chunks from a vector database and passes them to the language model as context.

## ✨ Key Features

- **PDF-Based Question Answering:** Ask questions related to your documents.
- **Semantic Search:** Retrieve relevant content based on meaning.
- **Local Embeddings:** Generate embeddings using Hugging Face.
- **Vector Database:** Store and retrieve document embeddings using ChromaDB.
- **MMR Retrieval:** Retrieve relevant and diverse document chunks.
- **LLM Integration:** Generate natural-language answers using Groq.
- **Context-Aware Responses:** Generate answers using retrieved document context.
- **Interactive CLI:** Ask multiple questions in a single session.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | LLM application framework |
| Groq API | LLM inference |
| GPT-OSS-20B | Language model |
| Hugging Face | Embedding model |
| all-MiniLM-L6-v2 | Text embeddings |
| ChromaDB | Vector database |
| PyPDFLoader | PDF document loading |
| RecursiveCharacterTextSplitter | Document chunking |
| python-dotenv | Environment variable management |

## 🧠 How It Works

The project follows a Retrieval-Augmented Generation pipeline:

1. **Document Loading:** Load PDF documents using PyPDFLoader.
2. **Text Splitting:** Divide documents into smaller chunks.
3. **Embedding Generation:** Convert text chunks into numerical vectors.
4. **Vector Storage:** Store embeddings in ChromaDB.
5. **User Query:** Accept a question from the user.
6. **Retrieval:** Retrieve relevant chunks using MMR search.
7. **Prompt Construction:** Combine retrieved context with the user's question.
8. **LLM Generation:** Send the prompt to Groq's GPT-OSS-20B model.
9. **Response:** Display the generated answer.

## 🏗️ Architecture

```text
        PDF Documents
              |
              v
        PDF Document Loader
              |
              v
        Text Chunking
              |
              v
      Hugging Face Embeddings
              |
              v
         ChromaDB
       (Vector Storage)
              |
              |
       User Question
              |
              v
       MMR Retriever
              |
              v
      Relevant Text Chunks
              |
              v
       Prompt Template
              |
              v
       Groq LLM (GPT-OSS-20B)
              |
              v
        Generated Answer
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository.git
```

### 2. Navigate to the Project

```bash
cd your-repository
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

Install the packages used in the project:

```bash
pip install langchain langchain-groq langchain-community langchain-huggingface langchain-chroma langchain-text-splitters pypdf python-dotenv sentence-transformers
```

### 5. Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from [Groq Console](https://console.groq.com/keys).

**Important:** Never upload your `.env` file or expose your API key on GitHub.

### 6. Run the Application

After setting up your PDF ingestion and ChromaDB vector store:

```bash
python main.py
```

## 💬 Example Interaction

```text
Welcome to the ChatGroq PDF Assistant!
Type 0 to quit the program.

Enter your question: What is the full form of RAG?

Response: Retrieval-Augmented Generation

Enter your question: 0

Exiting the program. Goodbye!
```

## 📂 Project Structure

```text
RAG-Project/
│
├── main.py
├── .env
├── .gitignore
├── pyproject.toml
├── uv.lock
│
├── chroma_db/
│   └── Vector database files
│
└── README.md
```

*Note: Keep `.venv/`, `.env`, and generated database files out of GitHub unless you intentionally want to share them.*

## 🔮 Future Improvements

- Streamlit or React-based web interface.
- Support for multiple PDF uploads.
- Source citations with page numbers.
- Conversation memory for follow-up questions.
- Document-level filtering.
- Deployment using FastAPI.
- Support for additional document formats.

## 🎯 Learning Outcomes

Through this project, I explored:

- Retrieval-Augmented Generation (RAG).
- Embeddings and semantic search.
- Vector databases and similarity search.
- LangChain integration.
- Prompt engineering.
- LLM API integration.
- Building practical Generative AI applications.

## 👨‍💻 Author

**Kumar Divyansh**

B.Tech – Computer Science & Engineering

Interested in Artificial Intelligence, Machine Learning, Generative AI and Agentic AI.

---

⭐ If you find this project interesting, consider giving it a star!
