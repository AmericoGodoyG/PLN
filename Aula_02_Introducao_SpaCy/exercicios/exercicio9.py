# Exercício 9 - Similaridade Formatada entre Termos
# Objetivo: Calcular e exibir a similaridade entre pares de termos com formatação

import spacy

# Carrega o modelo de linguagem de português
nlp = spacy.load("pt_core_news_sm")

# Lista de frases/termos para comparação semântica
frases = [
    "inteligência artificial",
    "aprendizado de máquina",
    "futebol",
    "redes neurais"
]

# Processa cada frase com o spaCy para obter os vetores de cada uma
docs = [nlp(frase) for frase in frases]

print("Similaridade entre os termos:\n")

# Compara cada par único de termos e exibe a similaridade formatada com 3 decimais
for i in range(len(docs)):
    for j in range(i + 1, len(docs)):
        similaridade = docs[i].similarity(docs[j])
        print(f"{frases[i]}  <->  {frases[j]} : {similaridade:.3f}")