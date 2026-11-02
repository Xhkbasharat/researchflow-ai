
from database.connection import get_connection
from pgvector import Vector


def save_document_chunks(
    filename: str,
    chunks: list,
    embeddings: list
) -> int:
    """
    Save document chunks and embeddings in PostgreSQL.
    """

    if len(chunks) != len(embeddings):
        raise ValueError("Chunks and embeddings must match.")

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                INSERT INTO documents (filename)
                VALUES (%s)
                RETURNING id;
                """,
                (filename,)
            )

            document_id = cursor.fetchone()[0]

            for chunk, embedding in zip(chunks, embeddings):

                if len(embedding) != 1536:
                    raise ValueError(
                        "Embedding must contain 1536 dimensions."
                    )

                cursor.execute(
                    """
                    INSERT INTO document_chunks
                    (document_id, chunk_number, content, embedding)
                    VALUES (%s, %s, %s, %s);
                    """,
                    (
                        document_id,
                        chunk["chunk_id"],
                        chunk["content"],
                        Vector(embedding)
                    )
                )

        connection.commit()
        return document_id

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def search_similar_chunks(
    query_embedding: list,
    top_k: int = 5
) -> list:
    """
    Retrieve the most similar document chunks.
    """

    if len(query_embedding) != 1536:
        raise ValueError("Query embedding must have 1536 dimensions.")

    if top_k <= 0:
        raise ValueError("top_k must be positive.")

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT
                    document_id,
                    chunk_number,
                    content,
                    1 - (embedding <=> %s) AS similarity
                FROM document_chunks
                WHERE embedding IS NOT NULL
                ORDER BY embedding <=> %s
                LIMIT %s;
                """,
                (
                    Vector(query_embedding),
                    Vector(query_embedding),
                    top_k
                )
            )

            rows = cursor.fetchall()

            return [
                {
                    "document_id": row[0],
                    "chunk_number": row[1],
                    "content": row[2],
                    "similarity": float(row[3])
                }
                for row in rows
            ]

    finally:
        connection.close()
      
