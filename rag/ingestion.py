from tools.pdf_reader import extract_pdf_text
from rag.chunker import chunk_text
from rag.embeddings import generate_embeddings
from database.vector_store import save_document_chunks


def ingest_pdf(file_path: str) -> dict:
    """
    Extract, chunk, embed and store a PDF document.
    """

    # Step 1: Extract PDF text
    document = extract_pdf_text(file_path)

    if not document["text"].strip():
        raise ValueError("No extractable text found in PDF.")

    # Step 2: Divide text into chunks
    chunks = chunk_text(
        document["text"],
        chunk_size=1000,
        overlap=200
    )

    # Step 3: Generate embeddings in batches
    all_embeddings = []

    batch_size = 100

    for start in range(0, len(chunks), batch_size):
        batch = chunks[start:start + batch_size]

        texts = [
            chunk["content"] for chunk in batch
        ]

        embeddings = generate_embeddings(texts)
        all_embeddings.extend(embeddings)

    # Step 4: Save chunks and embeddings
    document_id = save_document_chunks(
        filename=document["filename"],
        chunks=chunks,
        embeddings=all_embeddings
    )

    return {
        "document_id": document_id,
        "filename": document["filename"],
        "total_pages": document["total_pages"],
        "total_chunks": len(chunks),
        "status": "success"
    }
  
