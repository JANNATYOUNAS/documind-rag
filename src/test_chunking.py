from extract_text import extract_text_from_pdf
from preprocess import preprocess_text
from chunking import chunk_text


pdf_path = "data/hospitals/IHRA-Standards-for-Hospitals.pdf"

# Extract text
raw_text = extract_text_from_pdf(pdf_path)

# Preprocess text
cleaned_text = preprocess_text(raw_text)

# Chunk text
chunks = chunk_text(cleaned_text)

print(f"\nTotal Chunks Created: {len(chunks)}\n")

for i, chunk in enumerate(chunks[:3]):

    print(f"\n--- Chunk {i+1} ---\n")

    print(chunk[:500])