from openai import OpenAI

client = OpenAI()


def fact_check_report(report: str, research_data: dict) -> str:
    """
    Evaluate report claims against collected research evidence.
    """

    sources = research_data.get("sources", [])

    if not sources:
        raise ValueError("No research sources available.")

    evidence = ""

    for index, source in enumerate(sources, start=1):
        evidence += f"""
        SOURCE {index}
        Title: {source.get('title', '')}
        URL: {source.get('url', '')}
        Evidence: {source.get('content', '')}
        """

    prompt = f"""
    You are an expert AI Fact-Checking Agent.

    RESEARCH REPORT:
    {report}

    ORIGINAL RESEARCH EVIDENCE:
    {evidence}

    Review the report and identify:

    1. Claims supported by the sources.
    2. Claims partially supported.
    3. Unsupported claims.
    4. Claims that contradict the evidence.
    5. Missing citations.
    6. Recommendations for corrections.

    RULES:
    - Never invent evidence.
    - Never assume a claim is true.
    - Distinguish unsupported from false.
    - Refer to source URLs where possible.
    - If evidence is insufficient, say so.

    End with an overall assessment:
    PASS, NEEDS REVISION, or INSUFFICIENT EVIDENCE.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text
  
