import spacy

#Carrega o modelo de linguagem de português
nlp = spacy.load("pt_core_news_sm")

texto = "O professor Tiago explicou PLN usando spaCy na Fatec."

doc = nlp(texto)

for token in doc:
    print(f"texto: {token.text:10} | "
        f"Lemma: {token.lemma_:10} | " 
        f"POS: {token.pos_:6} | "
        f"Stop: {token.is_stop}"
    )

print("\nEntidades:")
for ent in doc.ents:
    print(ent.text, ent.label_)

# Tokenização - Divirdir texto em unidades menores
# Lematização - Reduzir palavras à forma base
# POS Tagging - Classificar palavras gramaticalmente
# Stop Words - Remover palavras irrelevantes

# Parsing - Analisar estruturas sintática
# NER - Identificar entidades
# Embeddings - Representação vetorial semântica