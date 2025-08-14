import os
from langchain_groq import ChatGroq

def get_primary_llm(**kwargs):
    model = os.getenv("PRIMARY_GROQ_MODEL", "llama-3.3-70b-versatile")
    return ChatGroq(model=model, api_key=os.getenv("GROQ_API_KEY"), temperature=0.0, **kwargs)

def get_fallback_llm(**kwargs):
    model = os.getenv("FALLBACK_GROQ_MODEL", "llama-3.1-8b-instant")
    return ChatGroq(model=model, api_key=os.getenv("GROQ_API_KEY"), temperature=0.2, **kwargs)