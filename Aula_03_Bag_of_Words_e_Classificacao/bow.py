# Exemplo - Bag of Words (BoW) com scikit-learn
# Objetivo: Demonstrar como transformar textos em representação vetorial usando CountVectorizer

# Instalação do scikit-learn (descomente se necessário)
# %pip install scikit-learn

# Importa o CountVectorizer que converte textos em matrizes de contagem de tokens
from sklearn.feature_extraction.text import CountVectorizer

# Define o corpus: conjunto de documentos (frases) para análise
corpus = [
    "gosto de machine learning",
    "machine learning é incrível",
    "gosto de programar"
]

# Inicializa o vetorizador
vectorizer = CountVectorizer()

# fit_transform: aprende o vocabulário (fit) e transforma os textos em vetores (transform)
X = vectorizer.fit_transform(corpus)

# Exibe o vocabulário aprendido (palavras únicas em ordem alfabética)
print("Vocabulário")
print(vectorizer.get_feature_names_out())

# Exibe a matriz de contagem (cada linha = documento, cada coluna = palavra do vocabulário)
print("\nMatriz: ")
print(X.toarray())
