
from openai import OpenAI

client = OpenAI()


def generate_report(research_data, analysis_data):

    prompt = f"""
    You are an AI Research Report Writer.

    Research Findings:
    {research_data}

    Research Analysis:
    {analysis_data}

    Create a professional research report with
    the following sections:

    1. Title
    2. Executive Summary
    3. Introduction
    4. Research Findings
    5. Analysis and Insights
    6. Opportunities
    7. Risks and Limitations
    8. Conclusion

    Important:
    - Use clear professional language.
    - Do not invent facts or statistics.
    - Do not create fake references.
    - Mention missing information where necessary.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text


if __name__ == "__main__":

    research = """
    AI is being used in education for personalized
    learning and automated assessment.
    """

    analysis = """
    AI may help personalize learning, but its
    effectiveness depends on implementation
    and reliable educational data.
    """

    report = generate_report(research, analysis)

    print("\n===== FINAL RESEARCH REPORT =====\n")
    print(report)
  
