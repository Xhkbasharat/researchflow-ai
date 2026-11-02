
from typing import List, Dict


def chunk_text(
    text: str,
    chunk_size: int = 1000,
    overlap: int = 200
) -> List[Dict]:
    """
    Split document text into overlapping chunks.

    Each chunk retains its position in the document.
    """

    if not text or not text.strip():
        raise ValueError("Input text cannot be empty.")

    if chunk_size <= 0:
        raise ValueError("Chunk size must be positive.")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError(
            "Overlap must be between 0 and chunk_size."
        )

    chunks = []
    start = 0
    chunk_number = 1

    while start < len(text):
        end = min(start + chunk_size, len(text))

        content = text[start:end].strip()

        if content:
            chunks.append({
                "chunk_id": chunk_number,
                "start": start,
                "end": end,
                "content": content
            })

            chunk_number += 1

        if end == len(text):
            break

        start = end - overlap

    return chunks


if __name__ == "__main__":

    sample_text = """
    Artificial Intelligence is transforming education.
    It supports personalized learning and automation.
    """ * 100

    results = chunk_text(sample_text)

    print("Total chunks:", len(results))

    for chunk in results[:2]:
        print("\nChunk:", chunk["chunk_id"])
        print(chunk["content"])
      
