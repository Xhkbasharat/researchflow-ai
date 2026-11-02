
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def create_research_plan(topic: str) -> str:
    """
    Create a structured research plan for a given topic.
    """

    if not topic.strip():
        raise ValueError("Research topic cannot be empty.")

    prompt = f"""
    You are an expert AI Research Planner.

    Create a detailed research plan for this topic:

    {topic}

    Include:

    1. Research objective
    2. Main research questions
    3. Subtopics to investigate
    4. Information and evidence to collect
    5. Important risks or limitations
    6. Expected report structure

    Create a clear, logical plan.
    Do not invent research findings.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text


if __name__ == "__main__":
    plan = create_research_plan(
        "Impact of Artificial Intelligence on Education"
    )

    print("\n===== RESEARCH PLAN =====\n")
    print(plan)
  
