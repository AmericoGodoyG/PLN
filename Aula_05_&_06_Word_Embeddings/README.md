# Representações com Word Embeddings

## 🧠 O que é?
Os **Word Embeddings** (como o *Word2Vec, FastText ou GloVe*) representam um avanço gigantesco na fase de vetorização da PLN, superando técnicas puramente quantitativas e numéricas do passado (como o BoW ou TF-IDF limitados pela não contabilidade de relação lexical da frase).

Modelos de Embeddings alocam as palavras que usamos (um vocabulário inteiro) dentro de um espaço multivetorial contínuo, denso, e dimensional. As palavras são modeladas de forma semântica pelo contexto em sua lateral ("uma palavra se conhece pelas vizinhas de quem anda".). Sendo assim, os tensores das palavras Rei e Rainha estarão no mesmo campo de relevância contextual e a distância matemática entre eles é semelhante à diferença vetorial de Homem para Mulher.

## 🛠️ Principais Aplicações
- **Entendimento Semântico Complexo:** Extração de subtextos em análise de sentimentos profundas que envolvam metáforas, gírias e ironias.
- **Correções e Auto-completamentos Inteligentes:** Sugestões nos teclados prevendo o próximo conceito base.
- **Avanções de Deep Learning Textuais:** Representam a "Base Construtiva de Features" para alimentar desde de Redes Neurais Recorrentes (LSTMs) até aos Grandes Modelos de Linguagem GenAI.
