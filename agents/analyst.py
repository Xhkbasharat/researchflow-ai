from openai import OpenAI

client = OpenAI()


def analyze_research(topic: str, research_data: dict) -> str:
    """
    Analyze research findings and extract useful insights.
    """

    if not research_data.get("summary"):
        raise ValueError("Research summary is missing.")

    prompt = f"""
    You are an expert AI Research Analyst.

    RESEARCH TOPIC:
    {topic}

    RESEARCH FINDINGS:
    {research_data["summary"]}

    YOUR TASKS:

    1. Identify the five most important findings.
    2. Identify emerging trends.
    3. Explain potential opportunities.
    4. Identify risks and challenges.
    5. Compare different viewpoints.
    6. Identify gaps in the available research.
    7. Provide a conclusion.

    RULES:
    - Use only the supplied research findings.
    - Do not invent statistics or facts.
    - Distinguish evidence from interpretation.
    - Mention uncertainty where appropriate.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text
  
