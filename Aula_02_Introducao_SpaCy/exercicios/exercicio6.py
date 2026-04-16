import spacy
from collections import Counter

nlp = spacy.load("pt_core_news_sm")

texto = "A OpenAI foi fundada em 2015 e possui escritórios em São Francisco."

doc = nlp(texto)

entidades = []

for ent in doc.ents:
    print(ent.text, "-", ent.label_)
    entidades.append(ent.label_)

contador = Counter(entidades)

print("\nQuantidade por tipo:")
for tipo, qtd in contador.items():
    print(tipo, ":", qtd)