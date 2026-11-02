from openai import OpenAI

from rag.chunker import chunk_text
from rag.retriever import retrieve_relevant_chunks

client = OpenAI()


def answer_from_document(
    document_data: dict,
    question: str,
    top_k: int = 5
) -> dict:
    """
    Answer questions using relevant PDF document content.
    """

    if not question.strip():
        raise ValueError("Question cannot be empty.")

    document_text = document_data.get("text", "")

    if not document_text.strip():
        raise ValueError("Document contains no extractable text.")

    # Step 1: Divide document into chunks
    chunks = chunk_text(
        document_text,
        chunk_size=1000,
        overlap=200
    )

    # Step 2: Retrieve relevant chunks
    relevant_chunks = retrieve_relevant_chunks(
        query=question,
        chunks=chunks,
        top_k=top_k
    )

    # Step 3: Prepare evidence
    evidence = "\n\n".join(
        f"""
        Chunk {chunk['chunk_id']}
        Relevance: {chunk['similarity_score']:.3f}
        Content: {chunk['content']}
        """
        for chunk in relevant_chunks
    )

    # Step 4: Generate an evidence-based answer
    prompt = f"""
    You are an AI Document Research Assistant.

    DOCUMENT:
    {document_data.get('filename', 'Unknown')}

    USER QUESTION:
    {question}

    RETRIEVED DOCUMENT EVIDENCE:
    {evidence}

    INSTRUCTIONS:
    1. Answer using the retrieved evidence.
    2. Explain important findings.
    3. Mention relevant chunk numbers.
    4. Identify missing information.
    5. Never invent facts.
    6. If evidence is insufficient, say so.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return {
        "question": question,
        "answer": response.output_text,
        "retrieved_chunks": relevant_chunks
    }
    
