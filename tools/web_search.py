import os
from tavily import TavilyClient


def search_web(query: str, max_results: int = 5):
    """
    Search the web and return structured research results.
    """

    api_key = os.getenv("TAVILY_API_KEY")

    if not api_key:
        raise ValueError(
            "TAVILY_API_KEY is missing from environment variables."
        )

    client = TavilyClient(api_key=api_key)

    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=max_results,
        include_answer=True
    )

    results = []

    for item in response.get("results", []):
        results.append({
            "title": item.get("title", ""),
            "url": item.get("url", ""),
            "content": item.get("content", ""),
            "score": item.get("score", 0)
        })

    return {
        "query": query,
        "answer": response.get("answer", ""),
        "results": results
    }


if __name__ == "__main__":
    research = search_web(
        "Latest developments in Agentic AI"
    )

    print(research)
  
