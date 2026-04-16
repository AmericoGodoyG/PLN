import spacy

#Carrega o modelo de linguagem de português
nlp = spacy.load("pt_core_news_sm")
texto = "O professor Tiago explicou PLN usando spaCy na Fatec."
doc = nlp(texto)

qtde_verbo = 0
for token in doc:
    if token.pos_ == "VERB":
         print(f"{token.text:10} POS: {token.pos_:10} || DEP: {token.dep_:10} HEAD: {token.head.text}")
         qtde_verbo += 1
print(f"Quantidade de verbos: {qtde_verbo}")
