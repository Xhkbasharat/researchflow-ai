
from openai import OpenAI

client = OpenAI()


def fact_check_report(report, research_evidence):

    prompt = f"""
    You are an AI Fact-Checking Agent.

    Your task is to review a research report
    using only the supplied research evidence.

    RESEARCH REPORT:
    {report}

    RESEARCH EVIDENCE:
    {research_evidence}

    Check the report and provide:

    1. Claims supported by the evidence.
    2. Claims not supported by the evidence.
    3. Claims that contradict the evidence.
    4. Claims requiring additional sources.
    5. Overall fact-checking summary.

    Important rules:
    - Never invent evidence or sources.
    - Do not assume a claim is true.
    - Explain why a claim is unsupported.
    - Do not treat missing evidence as proof
      that a claim is false.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text


if __name__ == "__main__":

    sample_report = """
    AI can support personalized learning
    and automated assessment in education.
    """

    sample_evidence = """
    The supplied research notes state that
    AI is used for personalized learning
    and automated assessment.
    """

    result = fact_check_report(
        sample_report,
        sample_evidence
    )

    print("\n===== FACT CHECK REPORT =====\n")
    print(result)
  
