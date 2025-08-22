# search_tool/__init__.py

import requests
from decouple import config

TAVILY_API_KEY = config("TAVILY_API_KEY")

def web_search(query: str):
    url = "https://api.tavily.com/search"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TAVILY_API_KEY}"
    }
    payload = {
        "query": query,
        "search_depth": "basic",
        "include_answer": True,
        "include_sources": True
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}
