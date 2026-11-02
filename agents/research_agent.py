
from openai import OpenAI

client = OpenAI()


def research_topic(topic, source_text=""):
    prompt = f"""
    You are an AI Research Agent.

    Research topic: {topic}

    Available source information:
    {source_text if source_text else "No source information provided."}

    Instructions:
    1. Identify the main research questions.
    2. Summarize the available information.
    3. Identify important findings.
    4. Mention missing information.
    5. Never invent facts or sources.

    If no source information is provided,
    create a research plan instead of claiming
    that you have completed research.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text


if __name__ == "__main__":
    result = research_topic(
        "How is Artificial Intelligence changing education?"
    )
    print(result)
  
