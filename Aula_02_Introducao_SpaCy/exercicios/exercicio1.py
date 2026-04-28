# Exercício 1 - Tokenização básica com spaCy
# Objetivo: Carregar um texto, tokenizá-lo e contar os tokens (excluindo pontuação)

import spacy

# Carrega o modelo de linguagem de português (versão pequena)
nlp = spacy.load("pt_core_news_sm")

# Define o texto de exemplo para análise
texto = "A inteligência artificial está transformando a educação superior no Brasil."

# Processa o texto através do pipeline do spaCy, gerando um objeto Doc
doc = nlp(texto)

# Inicializa o contador de tokens
count = 0

# Itera sobre cada token do documento, ignorando o ponto final
for token in doc:
    if token.text != '.':
        print(f"texto: {token.text:10}")
        count += 1

# Exibe a quantidade total de tokens encontrados (sem pontuação)
print(count)
