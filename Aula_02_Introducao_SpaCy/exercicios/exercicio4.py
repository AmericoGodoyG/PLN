import spacy
from collections import Counter

nlp = spacy.load("pt_core_news_sm")

texto = """
A inteligência artificial está transformando o mundo. 
Empresas utilizam aprendizado de máquina para analisar dados 
e melhorar decisões. Muitas organizações investem em tecnologia.
"""

doc = nlp(texto)

palavras_limpas = []

for token in doc:
    if not token.is_stop and not token.is_punct and len(token.text) >= 3:
        palavras_limpas.append(token.text.lower())

print("Palavras limpas:")
print(palavras_limpas)

frequencia = Counter(palavras_limpas)

print("\n5 palavras mais frequentes:")
for palavra, freq in frequencia.most_common(5):
    print(palavra, ":", freq)