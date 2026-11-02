
from openai import OpenAI

client = OpenAI()


def generate_report(
    topic: str,
    research_data: dict,
    analysis: str
) -> str:
    """
    Generate a structured research report.
    """

    if not research_data.get("summary"):
        raise ValueError("Research evidence is missing.")

    sources = research_data.get("sources", [])

    source_list = "\n".join(
        f"- {source['title']}: {source['url']}"
        for source in sources
    )

    prompt = f"""
    You are a professional AI Research Report Writer.

    RESEARCH TOPIC:
    {topic}

    RESEARCH FINDINGS:
    {research_data["summary"]}

    ANALYSIS:
    {analysis}

    AVAILABLE SOURCES:
    {source_list}

    Generate a professional research report with:

    1. Title
    2. Executive Summary
    3. Introduction
    4. Research Methodology
    5. Key Findings
    6. Detailed Analysis
    7. Opportunities
    8. Risks and Challenges
    9. Limitations
    10. Conclusion
    11. References

    RULES:
    - Use professional language.
    - Do not invent facts or statistics.
    - Use only the supplied research evidence.
    - Include source URLs where relevant.
    - Clearly identify limitations.
    - Do not create fake references.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text
  
