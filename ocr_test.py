from pdf2image import convert_from_path # type: ignore
import pytesseract # type: ignore


def ocr_pages(pdf_path, first_page, last_page):
    pages = convert_from_path(
        pdf_path,
        first_page=first_page,
        last_page=last_page
    )

    results = []

    for page_number, page in enumerate(pages, start=first_page):
        text = pytesseract.image_to_string(page)

        results.append(
            f"\n{'=' * 60}\n"
            f"PAGE {page_number}\n"
            f"{'=' * 60}\n"
            f"{text}"
        )

    return "\n".join(results)


pdf_path = "data/raw/companies_house_document.pdf"

text = ocr_pages(pdf_path, 4, 6)

with open("data/processed_leicester_financials.txt", "w") as file:
    file.write(text)

print("OCR extraction saved.")