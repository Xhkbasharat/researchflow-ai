import os
import psycopg

from pgvector.psycopg import register_vector


def get_connection():
    """
    Create a PostgreSQL connection with pgvector support.
    """

    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise ValueError(
            "DATABASE_URL is missing from environment variables."
        )

    connection = psycopg.connect(database_url)

    register_vector(connection)

    return connection


def test_connection():
    """Check whether the database connection works."""

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT version();")
            result = cursor.fetchone()

            print("Database connection successful!")
            print(result[0])

    finally:
        connection.close()


if __name__ == "__main__":
    test_connection()
  
