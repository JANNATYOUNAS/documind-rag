from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class TFIDFRetriever:

    def __init__(self):

        self.vectorizer = TfidfVectorizer()

        self.chunk_vectors = None

        self.chunks = None

    def fit(self, chunks):

        self.chunks = chunks

        self.chunk_vectors = self.vectorizer.fit_transform(chunks)

    def retrieve(self, query, top_k=3):

        # Convert query into TF-IDF vector
        query_vector = self.vectorizer.transform([query])

        # Compute similarity
        similarities = cosine_similarity(
            query_vector,
            self.chunk_vectors
        ).flatten()

        # Get top matching chunks
        top_indices = similarities.argsort()[-top_k:][::-1]

        results = []

        for idx in top_indices:

            results.append({
                "chunk": self.chunks[idx],
                "score": similarities[idx]
            })

        return results