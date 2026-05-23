import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()


def preprocess_text(text):

    # Convert to lowercase
    text = text.lower()

    # Remove numbers
    text = re.sub(r'\d+', '', text)

    # Remove punctuation/special characters
    text = re.sub(r'[^\w\s]', '', text)

    # Tokenization
    tokens = word_tokenize(text)

    # Remove stopwords
    filtered_tokens = []

    for word in tokens:

        if word not in stop_words:
            filtered_tokens.append(word)

    # Stemming
    stemmed_tokens = []

    for word in filtered_tokens:
        stemmed_tokens.append(stemmer.stem(word))

    # Join words back into sentence
    cleaned_text = " ".join(stemmed_tokens)

    return cleaned_text