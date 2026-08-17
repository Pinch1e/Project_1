from pathlib import Path
from pypdf import PdfReader # type: ignore 

pdf_path = Path("data/raw/companies_house_document.pdf")

reader = PdfReader(pdf_path)

print(f"Number of pages: {len(reader.pages)}")

for page_number, page in enumerate(reader.pages):
    text = page.extract_text() or ""

    print(f"Page {page_number +1}: {len(text)} characters")

