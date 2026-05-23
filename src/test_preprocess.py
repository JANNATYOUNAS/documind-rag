from preprocess import preprocess_text

sample_text = """
The doctors are available in the emergency ward 24 hours daily.
"""

cleaned = preprocess_text(sample_text)

print(cleaned)