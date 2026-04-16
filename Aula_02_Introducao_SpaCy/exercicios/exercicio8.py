import spacy

nlp = spacy.load("pt_core_news_sm")

palavras = [
    "inteligência artificial",
    "aprendizado de máquina",
    "futebol",
    "redes neurais"
]

docs = [nlp(p) for p in palavras]

for i in range(len(docs)):
    for j in range(i+1, len(docs)):
        sim = docs[i].similarity(docs[j])
        print(palavras[i], "-", palavras[j], ":", sim)