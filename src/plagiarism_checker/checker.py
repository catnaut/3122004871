from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def cal_tf_idf(texts: list):
    vectorizer = TfidfVectorizer()
    tf_idf = vectorizer.fit_transform([" ".join(text) for text in texts])
    return tf_idf


def cal_cosine_similarity(vectors):
    similarity_matrix = cosine_similarity(vectors)
    return similarity_matrix
