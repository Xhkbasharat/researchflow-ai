
from database.connection import get_connection


def initialize_database():
    """
    Create ResearchFlow AI database tables.
    """

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            # Enable vector extension
            cursor.execute(
                "CREATE EXTENSION IF NOT EXISTS vector;"
            )

            # Research documents
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS documents (
                    id BIGSERIAL PRIMARY KEY,
                    filename TEXT NOT NULL,
                    created_at TIMESTAMPTZ DEFAULT NOW()
                );
            """)

            # Document chunks and embeddings
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS document_chunks (
                    id BIGSERIAL PRIMARY KEY,
                    document_id BIGINT REFERENCES documents(id)
                        ON DELETE CASCADE,
                    chunk_number INTEGER NOT NULL,
                    content TEXT NOT NULL,
                    embedding VECTOR(1536),
                    created_at TIMESTAMPTZ DEFAULT NOW()
                );
            """)

            # Generated research reports
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS research_reports (
                    id BIGSERIAL PRIMARY KEY,
                    topic TEXT NOT NULL,
                    report TEXT NOT NULL,
                    fact_check TEXT,
                    review TEXT,
                    created_at TIMESTAMPTZ DEFAULT NOW()
                );
            """)

        connection.commit()
        print("ResearchFlow AI database initialized!")

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


if __name__ == "__main__":
    initialize_database()
  
