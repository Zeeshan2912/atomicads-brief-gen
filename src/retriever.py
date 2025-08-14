from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

def create_vectorstore(docs, persist_directory="./chroma_store"):
    hf = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    texts = [d["text"] for d in docs]
    metadatas = [d.get("metadata", {}) for d in docs]
    chroma = Chroma.from_texts(texts, embedding=hf, metadatas=metadatas, persist_directory=persist_directory)
    chroma.persist()
    return chroma