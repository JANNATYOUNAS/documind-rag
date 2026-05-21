import os
import pdfplumber

DATA_PATH = "data"


def extract_text_from_pdf(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

    return text


def process_documents():
    for root, dirs, files in os.walk(DATA_PATH):

        for file in files:

            if file.endswith(".pdf"):

                file_path = os.path.join(root, file)

                print(f"\nProcessing: {file}")

                extracted_text = extract_text_from_pdf(file_path)

                print(extracted_text[:1000])
                print("\n" + "=" * 50)


if __name__ == "__main__":
    process_documents()