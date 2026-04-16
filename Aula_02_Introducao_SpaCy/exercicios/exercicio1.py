import spacy

nlp = spacy.load("pt_core_news_sm")
texto = "A inteligência artificial está transformando a educação superior no Brasil."
doc = nlp(texto)

count = 0
for token in doc:
    if token.text != '.':
        print(f"texto: {token.text:10}")
        count += 1
print(count)
