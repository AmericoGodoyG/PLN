# Exercício 6 - Reconhecimento de Entidades Nomeadas (NER)
# Objetivo: Identificar entidades no texto e contar por tipo (PER, ORG, LOC, etc.)

import spacy
from collections import Counter

# Carrega o modelo de linguagem de português
nlp = spacy.load("pt_core_news_sm")

# Texto de exemplo contendo entidades nomeadas (organização, data e localidade)
texto = "A OpenAI foi fundada em 2015 e possui escritórios em São Francisco."

# Processa o texto com o spaCy
doc = nlp(texto)

# Lista para armazenar os tipos (labels) de cada entidade encontrada
entidades = []

# Itera sobre as entidades reconhecidas e exibe texto + tipo
for ent in doc.ents:
    print(ent.text, "-", ent.label_)
    entidades.append(ent.label_)

# Conta a quantidade de entidades por tipo usando Counter
contador = Counter(entidades)

# Exibe o resumo da contagem por tipo de entidade
print("\nQuantidade por tipo:")
for tipo, qtd in contador.items():
    print(tipo, ":", qtd)