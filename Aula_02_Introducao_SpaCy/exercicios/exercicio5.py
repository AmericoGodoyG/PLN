# Exercício 5 - Frequência completa de palavras relevantes
# Objetivo: Filtrar stop words/pontuação e listar TODAS as palavras por frequência

import spacy
from collections import Counter

# Carrega o modelo de linguagem de português
nlp = spacy.load("pt_core_news_sm")

# Texto de exemplo para análise de frequência
texto = """
A inteligência artificial está transformando o mundo.
Empresas utilizam aprendizado de máquina para analisar dados.
"""

# Processa o texto com o spaCy
doc = nlp(texto)

# Lista para armazenar palavras filtradas
palavras = []

# Filtra tokens removendo stop words, pontuação e palavras curtas (< 3 chars)
for token in doc:
    if not token.is_stop and not token.is_punct and len(token.text) >= 3:
        palavras.append(token.text.lower())

# Conta a frequência de cada palavra
frequencia = Counter(palavras)

# Exibe todas as palavras ordenadas por frequência (da mais para a menos frequente)
print("Frequência das palavras:")

for palavra, freq in frequencia.most_common():
    print(palavra, ":", freq)