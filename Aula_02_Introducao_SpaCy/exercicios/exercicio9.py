import spacy

nlp = spacy.load("pt_core_news_sm")

frases = [
    "inteligência artificial",
    "aprendizado de máquina",
    "futebol",
    "redes neurais"
]

docs = [nlp(frase) for frase in frases]

print("Similaridade entre os termos:\n")

for i in range(len(docs)):
    for j in range(i + 1, len(docs)):
        similaridade = docs[i].similarity(docs[j])
        print(f"{frases[i]}  <->  {frases[j]} : {similaridade:.3f}")