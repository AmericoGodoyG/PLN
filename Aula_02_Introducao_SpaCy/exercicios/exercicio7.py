import spacy

nlp = spacy.load("pt_core_news_sm")

texto = "O professor explicou aprendizado de máquina aos alunos."
doc = nlp(texto)

for token in doc:

    if token.dep_ == "ROOT":
        verbo = token.text

    if token.dep_ == "nsubj":
        sujeito = token.text

    if token.dep_ == "obj":
        objeto = token.text

print("Sujeito:", sujeito)
print("Verbo:", verbo)
print("Objeto:", objeto)