from pathlib import Path
from pypdf import PdfReader


def extract_pdf_text(file_path: str) -> dict:
    """
    Extract text and metadata from a PDF document.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"PDF file not found: {file_path}"
        )

    if path.suffix.lower() != ".pdf":
        raise ValueError("Only PDF files are supported.")

    reader = PdfReader(str(path))

    if reader.is_encrypted:
        raise ValueError("Encrypted PDFs are not supported.")

    pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        pages.append({
            "page": page_number,
            "content": text
        })

    full_text = "\n".join(
        page["content"] for page in pages
    )

    return {
        "filename": path.name,
        "total_pages": len(reader.pages),
        "text": full_text,
        "pages": pages
    }


if __name__ == "__main__":
    result = extract_pdf_text("sample.pdf")

    print("Filename:", result["filename"])
    print("Pages:", result["total_pages"])
    print(result["text"])
  
