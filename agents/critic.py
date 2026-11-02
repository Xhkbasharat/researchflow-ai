from openai import OpenAI

client = OpenAI()


def review_report(
    topic: str,
    report: str,
    fact_check: str
) -> str:
    """
    Review research report quality and recommend improvements.
    """

    if not report.strip():
        raise ValueError("Research report cannot be empty.")

    prompt = f"""
    You are an expert AI Research Quality Reviewer.

    RESEARCH TOPIC:
    {topic}

    GENERATED REPORT:
    {report}

    FACT-CHECK RESULTS:
    {fact_check}

    Evaluate the report using these criteria:

    1. Relevance to the research topic.
    2. Clarity and readability.
    3. Logical structure.
    4. Evidence quality.
    5. Citation completeness.
    6. Coverage of important research questions.
    7. Accuracy concerns identified by fact-checking.

    Provide:

    - Overall quality score out of 10.
    - Strengths of the report.
    - Weaknesses and missing information.
    - Specific improvement recommendations.
    - Final review decision:
      APPROVED, NEEDS REVISION, or REJECTED.

    RULES:
    - Do not invent evidence.
    - Do not change fact-check results.
    - Explain the reasons for your decision.
    - Be objective and specific.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text
  
