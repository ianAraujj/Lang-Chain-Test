# LangChain

* It's a framework that allows the use of LLM (Large Language Model)
* Allows an integration with several IA's such as: OpenAI

## LLM

* It's a type of neural network that learns from language. She learns from books, articles and internet texts.

### Funcionamento

1. Transform words into numbers (TOKENIZATION).
2. Calcular a distância entre os tokens.
3. Definir modelo que irá realizar o cálculo dessas proximidades. Esse modelo seria o Modelo dos Transformers.

## Transformers

* É uma arquitetura de redes neurais profunda.
* É uma arquitetura 'sequence-to-sequence': entrada é um texto e a saída é texto.
* É composta por 2 componentes:
  * 1 - ENCODER: codifica a entrada. A codificação dos tokens pode ser feita de forma paralela.
  * 2 - DECODER: recebe a saída do encoder e gera a saída final em texto. A decodificação da saída é feita um token por vez (não paralelizada), pois um token gerado é levado em consideração para gerar os próximos, esse é o conceito de `Auto regressivo`

* Camada do Encoder:
  * 1 - Self-Attention: mecanismo de atenção. Quando for feita a representação de uma palavra, serão observadas outras palavras na sentença que tenham alguma relevância. Isso porque algumas palavras na sentenças são mais importantes do que outras. Isso é feito, pois o contexto é muito importante na interpretação.
  * 2 - Feed Forward Neural Network: rede neural normal.

* Camada do Decoder: possui dois mecanismos de atenção.
  * 1 - Self-Attention: para gerar a próxima palavra, serão observadas as palavras que foram geradas antes, dando mais ênfase nas palavras mais importantes.
  * 2 - Encoder-Decoder Attention
  * 3 - Feed Forward Neural Network: rede neural normal.

* Permite paralelização, o que reduz o tempo de treinamento.

## Rede Neural

Composta:

    * CAMADA DE ENTRADA

    * CAMADAS OCULTAS

    * CAMADA DE SAÌDA

## Deep Learning

* Redes neurais com várias camadas ocultas

## Project Setup

### 1. The first thing you'll need to do is choose which `Chat Model` you want to use

If you've ever used an interface like ChatGPT before, the basic idea of a Chat Model will be familiar to you – the model takes messages as input, and returns messages as output.

### 2. Install packages

`pip install langchain_core langchain_anthropic`

https://www.freecodecamp.org/news/beginners-guide-to-langchain/