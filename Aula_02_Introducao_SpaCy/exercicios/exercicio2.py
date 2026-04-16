import spacy

#Carrega o modelo de linguagem de português
nlp = spacy.load("pt_core_news_sm")

texto = "Os alunos estavam estudando algoritmos e implementaram soluções eficientes"

doc = nlp(texto)

for token in doc:
    print(f"texto: {token.text:10} | "
        f"Lemma: {token.lemma_:10} | " 
    )

for carac in range(3):
    print("\n*")

for token in doc:
    print(f"Texto: {token.text:10} -> Lemma {token.lemma_:10}")