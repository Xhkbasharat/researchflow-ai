
import os
from tavily import TavilyClient


def search_web(query: str, max_results: int = 5):
    """Search the web and collect research sources."""

    api_key = os.getenv("TAVILY_API_KEY")

    if not api_key:
        raise ValueError("TAVILY_API_KEY is not configured.")

    client = TavilyClient(api_key=api_key)

    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=max_results
    )

    sources = []

    for item in response.get("results", []):
        sources.append({
            "title": item.get("title", ""),
            "url": item.get("url", ""),
            "content": item.get("content", ""),
            "score": item.get("score", 0)
        })

    return {
        "query": query,
        "sources": sources
    }


if __name__ == "__main__":
    result = search_web("Latest developments in Agentic AI")

    for source in result["sources"]:
        print("\nTitle:", source["title"])
        print("URL:", source["url"])
        print("Content:", source["content"])
      
