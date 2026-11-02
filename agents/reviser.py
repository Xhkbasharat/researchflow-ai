from openai import OpenAI

client = OpenAI()


def revise_report(
    topic: str,
    report: str,
    fact_check: str,
    critic_feedback: str,
    research_evidence: str
) -> str:
    """Improve a report using review feedback and evidence."""

    prompt = f"""
    You are an expert Research Report Revision Agent.

    RESEARCH TOPIC:
    {topic}

    CURRENT REPORT:
    {report}

    FACT-CHECK FEEDBACK:
    {fact_check}

    CRITIC FEEDBACK:
    {critic_feedback}

    ORIGINAL RESEARCH EVIDENCE:
    {research_evidence}

    TASK:
    Produce an improved version of the report.

    REQUIREMENTS:
    1. Correct unsupported or inaccurate claims.
    2. Address the critic's recommendations.
    3. Improve clarity and organization.
    4. Preserve valid findings.
    5. Keep relevant source URLs.
    6. Do not invent facts, statistics or citations.
    7. Clearly acknowledge remaining evidence gaps.

    Return the complete revised report.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text
  
