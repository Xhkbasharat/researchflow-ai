import math

from rag.embeddings import generate_embeddings


def cosine_similarity(vector_a, vector_b):
    """Calculate cosine similarity between two vectors."""

    if len(vector_a) != len(vector_b):
        raise ValueError("Embedding dimensions do not match.")

    dot_product = sum(
        a * b for a, b in zip(vector_a, vector_b)
    )

    magnitude_a = math.sqrt(sum(a * a for a in vector_a))
    magnitude_b = math.sqrt(sum(b * b for b in vector_b))

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (magnitude_a * magnitude_b)


def retrieve_relevant_chunks(
    query: str,
    chunks: list[dict],
    top_k: int = 5
) -> list[dict]:
    """
    Retrieve the most relevant chunks using embeddings.
    """

    if not query.strip():
        raise ValueError("Search query cannot be empty.")

    if not chunks:
        return []

    if top_k <= 0:
        raise ValueError("top_k must be positive.")

    texts = [chunk["content"] for chunk in chunks]

    # Generate embeddings for query and document chunks
    all_vectors = generate_embeddings([query] + texts)

    query_vector = all_vectors[0]
    document_vectors = all_vectors[1:]

    results = []

    for chunk, vector in zip(chunks, document_vectors):
        score = cosine_similarity(query_vector, vector)

        results.append({
            **chunk,
            "similarity_score": score
        })

    results.sort(
        key=lambda item: item["similarity_score"],
        reverse=True
    )

    return results[:top_k]
  
