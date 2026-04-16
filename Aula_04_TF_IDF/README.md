# Term Frequency - Inverse Document Frequency (TF-IDF)

## 🧠 O que é?
O **TF-IDF** (Frequência do Termo - Inverso da Frequência no Documento) é uma modelagem estatística usada na mineração e busca por dados textuais. É aprimoramento em relação à técnica Bag of Words (BoW). 

Enquanto o Bag of Words apenas conta a quantidade de palavras, supervalorizando termos vazios como "um", "de", "e" e "o" (se estes não forem filtrados), o **TF-IDF penaliza essas palavras frequentes no escopo geral** e recompensa o peso de palavras específicas e raras, que carregam os reais significados diferenciadores entre dezenas de documentos diferentes.

## 🛠️ Principais Aplicações
- **Recuperação da Informação e Motores de Busca:** Para calcular como os sites web devem ser ordenados ou pontuados dependendo da query exigida (ex. os precursores da indexação do Google ou sistemas locais em um comércio eletrônico).
- **Extração de Palavras-Chave:** Encontrar autonomamente quais são as três ou quatro palavras que melhor resumem uma página inteira de texto.
- **Pesagem de Atributos:** Alimentar Sistemas de Recomendação ou Modelos KNN focados em similaridade de tópicos.
