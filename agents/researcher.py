
from openai import OpenAI
from tools.web_search import search_web


client = OpenAI()


def conduct_research(topic: str, research_plan: str):
    """
    Search the web and prepare an evidence-based
    research summary.
    """

    if not topic.strip():
        raise ValueError("Research topic cannot be empty.")

    # Search the internet using Tavily
    search_results = search_web(
        query=topic,
        max_results=5
    )

    sources = search_results["sources"]

    if not sources:
        raise ValueError("No research sources were found.")

    # Prepare source information
    evidence = ""

    for index, source in enumerate(sources, start=1):
        evidence += f"""
        SOURCE {index}
        Title: {source['title']}
        URL: {source['url']}
        Content: {source['content']}
        """

    prompt = f"""
    You are an expert AI Research Agent.

    RESEARCH TOPIC:
    {topic}

    RESEARCH PLAN:
    {research_plan}

    WEB RESEARCH EVIDENCE:
    {evidence}

    Your tasks:

    1. Summarize the available evidence.
    2. Identify important findings.
    3. Compare information across sources.
    4. Identify conflicting information.
    5. Identify missing information.
    6. Include source URLs with relevant findings.

    IMPORTANT:
    - Use only the supplied source information.
    - Never invent facts or statistics.
    - Do not create fake citations.
    - Clearly identify unsupported claims.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return {
        "topic": topic,
        "summary": response.output_text,
        "sources": sources
    }
  
