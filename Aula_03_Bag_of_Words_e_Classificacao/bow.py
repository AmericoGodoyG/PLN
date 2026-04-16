# %pip install scikit-learn
from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    "gosto de machine learning",
    "machine learning é incrível",
    "gosto de programar"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

print("Vocabulário")
print(vectorizer.get_feature_names_out())

print("\nMatriz: ")
print(X.toarray())