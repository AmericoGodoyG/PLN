# Exercício 4 - Limpeza de texto e análise de frequência de palavras
# Objetivo: Remover stop words e pontuação, e encontrar as palavras mais frequentes

import spacy
from collections import Counter

# Carrega o modelo de linguagem de português
nlp = spacy.load("pt_core_news_sm")

# Texto de exemplo com múltiplas frases para análise
texto = """
A inteligência artificial está transformando o mundo. 
Empresas utilizam aprendizado de máquina para analisar dados 
e melhorar decisões. Muitas organizações investem em tecnologia.
"""

# Processa o texto com o spaCy
doc = nlp(texto)

# Lista para armazenar as palavras após limpeza
palavras_limpas = []

# Filtra tokens: remove stop words, pontuação e palavras com menos de 3 caracteres
for token in doc:
    if not token.is_stop and not token.is_punct and len(token.text) >= 3:
        palavras_limpas.append(token.text.lower())

# Exibe a lista de palavras limpas
print("Palavras limpas:")
print(palavras_limpas)

# Conta a frequência de cada palavra usando Counter
frequencia = Counter(palavras_limpas)

# Exibe as 5 palavras mais frequentes no texto
print("\n5 palavras mais frequentes:")
for palavra, freq in frequencia.most_common(5):
    print(palavra, ":", freq)