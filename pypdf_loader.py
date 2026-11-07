from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader('energy1.pdf')
docs =loader.load()
print(len(docs))