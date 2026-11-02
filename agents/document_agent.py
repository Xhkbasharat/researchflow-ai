
from openai import OpenAI

client = OpenAI()


def analyze_document(document_data: dict) -> str:
    """
    Analyze extracted PDF document content.
    """

    if not document_data.get("text"):
        raise ValueError("Document contains no extractable text.")

    document_text = document_data["text"]

    # Keep the initial implementation within a manageable
    # context size. We'll add chunking and RAG later.
    document_text = document_text[:30000]

    prompt = f"""
    You are an AI Document Research Agent.

    DOCUMENT:
    {document_data.get("filename", "Unknown document")}

    TOTAL PAGES:
    {document_data.get("total_pages", 0)}

    EXTRACTED CONTENT:
    {document_text}

    YOUR TASKS:

    1. Summarize the document.
    2. Identify its main topics.
    3. Extract important findings.
    4. Identify useful statistics and data.
    5. Identify limitations and research gaps.
    6. Mention relevant page numbers when available.

    RULES:
    - Use only the supplied document content.
    - Do not invent facts or statistics.
    - Preserve important numerical information.
    - Mention if the document lacks sufficient evidence.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text
  
