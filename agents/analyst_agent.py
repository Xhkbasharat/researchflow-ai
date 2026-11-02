from openai import OpenAI

client = OpenAI()


def analyze_research(research_data):

    prompt = f"""
    You are an AI Research Analyst.

    Analyze the following research findings:

    {research_data}

    Your tasks:
    1. Identify the key findings.
    2. Identify important trends.
    3. Explain opportunities.
    4. Identify possible risks.
    5. Provide a clear conclusion.

    Use only the information provided.
    Do not invent facts or statistics.
    Clearly mention missing information.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text


if __name__ == "__main__":

    sample_research = """
    Artificial Intelligence is increasingly used
    in education for personalized learning,
    automated assessment, and student support.
    """

    result = analyze_research(sample_research)

    print("\n===== RESEARCH ANALYSIS =====\n")
    print(result)
  
