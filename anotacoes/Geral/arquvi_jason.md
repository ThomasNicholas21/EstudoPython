
# JSON
- Estrutura de dados criada para transportar ou salvar dados, sendo ela simplificada, similar ao objeto no JS e dicionário em Python.

## Tipos de dados
- Booleano
- Inteiro
- Float
- String
- Array (equivalente a lista em Python)
- Objeto (equivalente a dicionário em Python)

## Principais Funcionalidades
- **Interoperabilidade**: JSON é compatível com várias linguagens de programação, facilitando a troca de dados entre diferentes sistemas.
- **Facilidade de Leitura e Escrita**: É uma estrutura simples e legível tanto por humanos quanto por máquinas.
- **Serialização e Desserialização**: Conversão de objetos complexos para uma string JSON (serialização) e conversão de uma string JSON para um objeto (desserialização).
- **Uso Amplamente Difundido**: É o formato padrão para comunicação em APIs RESTful e na transferência de dados na web.

## Exemplos em Python

### Salvando dados em um arquivo JSON (serialização)
```python
import json

dados = {
    "nome": "João",
    "idade": 30,
    "casado": True,
    "filhos": ["Ana", "Pedro"]
}

with open("dados.json", "w") as arquivo:
    json.dump(dados, arquivo)
```

### Lendo dados de um arquivo JSON (desserialização)
```python
import json

with open("dados.json", "r") as arquivo:
    dados = json.load(arquivo)
    print(dados)
```

### Explicação dos métodos:
- **json.dump()**: Escreve um objeto Python (dicionário, lista, etc.) em um arquivo no formato JSON.
- **json.load()**: Lê um arquivo JSON e converte seu conteúdo para um objeto Python.
- **json.dumps()**: Escreve uma string Python em um arquivo no formato JSON.
- **json.loads()**: Lê uma string e converte seu conteúdo para um objeto.
