import spacy
from collections import Counter

nlp = spacy.load("pt_core_news_sm")

texto = """
A inteligência artificial está transformando o mundo.
Empresas utilizam aprendizado de máquina para analisar dados.
"""

doc = nlp(texto)

palavras = []

for token in doc:
    if not token.is_stop and not token.is_punct and len(token.text) >= 3:
        palavras.append(token.text.lower())

frequencia = Counter(palavras)

print("Frequência das palavras:")

for palavra, freq in frequencia.most_common():
    print(palavra, ":", freq)