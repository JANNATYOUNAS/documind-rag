from extract_text import extract_text_from_pdf
from preprocess import preprocess_text
from chunking import chunk_text
from retrieval import TFIDFRetriever


pdf_path = pdf_path = "data/hospitals/IHRA-Standards-for-Hospitals.pdf"

# Extract text
raw_text = extract_text_from_pdf(pdf_path)

# Preprocess
cleaned_text = preprocess_text(raw_text)

# Chunking
chunks = chunk_text(cleaned_text)

# Create retriever
retriever = TFIDFRetriever()

# Train retriever on chunks
retriever.fit(chunks)

# User query
query = "What are emergency department timings?"

# Retrieve results
results = retriever.retrieve(query)

# Display results
for i, result in enumerate(results):

    print(f"\n--- Result {i+1} ---")

    print(f"Similarity Score: {result['score']:.4f}")

    print(result["chunk"][:500])