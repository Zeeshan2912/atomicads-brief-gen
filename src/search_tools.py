from langchain_community.utilities import SerpAPIWrapper
import os

def web_search(query: str):
    wrapper = SerpAPIWrapper(serpapi_api_key=os.getenv("SERPAPI_API_KEY"))
    return wrapper.run(query)