# Exercício 8 - Cálculo de Similaridade entre Termos
# Objetivo: Comparar a similaridade semântica entre pares de frases/termos

import spacy

# Carrega o modelo de linguagem de português (sm usa vetores simples)
nlp = spacy.load("pt_core_news_sm")

# Lista de termos/expressões para comparar entre si
palavras = [
    "inteligência artificial",
    "aprendizado de máquina",
    "futebol",
    "redes neurais"
]

# Processa cada termo com o spaCy, gerando objetos Doc com vetores
docs = [nlp(p) for p in palavras]

# Compara cada par de termos (sem repetição) usando similaridade de cosseno
for i in range(len(docs)):
    for j in range(i+1, len(docs)):
        sim = docs[i].similarity(docs[j])
        print(palavras[i], "-", palavras[j], ":", sim)