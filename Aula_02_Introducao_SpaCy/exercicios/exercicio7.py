# Exercício 7 - Extração de Sujeito, Verbo e Objeto (Análise de Dependências)
# Objetivo: Usar a análise de dependências sintáticas para extrair a estrutura SVO

import spacy

# Carrega o modelo de linguagem de português
nlp = spacy.load("pt_core_news_sm")

# Texto de exemplo com estrutura clara de sujeito-verbo-objeto
texto = "O professor explicou aprendizado de máquina aos alunos."
doc = nlp(texto)

# Itera sobre os tokens para identificar sujeito, verbo (raiz) e objeto
for token in doc:

    # ROOT indica o verbo principal da frase (raiz da árvore de dependências)
    if token.dep_ == "ROOT":
        verbo = token.text

    # nsubj indica o sujeito nominal da frase
    if token.dep_ == "nsubj":
        sujeito = token.text

    # obj indica o objeto direto do verbo
    if token.dep_ == "obj":
        objeto = token.text

# Exibe a estrutura SVO extraída da frase
print("Sujeito:", sujeito)
print("Verbo:", verbo)
print("Objeto:", objeto)