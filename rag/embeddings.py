from openai import OpenAI

client = OpenAI()

EMBEDDING_MODEL = "text-embedding-3-small"


def generate_embeddings(texts: list[str]) -> list[list[float]]:
    """
    Convert text chunks into numerical embeddings.
    """

    if not texts:
        raise ValueError("No text provided for embedding.")

    if any(not text.strip() for text in texts):
        raise ValueError("Text chunks cannot be empty.")

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=texts
    )

    # Preserve the original input order
    ordered_results = sorted(
        response.data,
        key=lambda item: item.index
    )

    return [
        item.embedding
        for item in ordered_results
    ]


if __name__ == "__main__":

    sample_texts = [
        "Artificial Intelligence in education.",
        "Machine learning in healthcare.",
        "Multi-agent AI systems."
    ]

    vectors = generate_embeddings(sample_texts)

    for index, vector in enumerate(vectors):
        print(f"Text {index + 1}")
        print("Vector dimensions:", len(vector))
        print("First five values:", vector[:5])
  
