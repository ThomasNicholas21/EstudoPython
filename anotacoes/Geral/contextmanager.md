# Criando Arquivos com Python

- Neste exemplo, usamos a função `open` para abrir um arquivo em Python.

## Context Manager - with

- Utilizando o **_with_** ao inicializar um método em Python para leitura de arquivo, o mesmo irá abri-lo, executá-lo e fechá-lo automaticamente.
    ```python
    with open(caminho_arquivo, 'w') as arquivo:
        print('Gerando Texto.')
        print('Fechando de forma automática.')
    ```

## Modos

- ### **'r'** (Leitura)
  Abre o arquivo para leitura. Se o arquivo não existir, ocorrerá um erro.
  ```python
  with open('arquivo.txt', 'r') as arquivo:
      conteudo = arquivo.read()
  ```

- ### **'w'** (Escrita)
  Abre o arquivo para escrita. Se o arquivo já existir, o conteúdo será sobrescrito. Caso contrário, cria um novo arquivo.
  ```python
  with open('arquivo.txt', 'w') as arquivo:
      arquivo.write('Novo conteúdo.')
  ```

- ### **'x'** (Criação)
  Cria um novo arquivo para escrita. Se o arquivo já existir, ocorrerá um erro.
  ```python
  with open('novo_arquivo.txt', 'x') as arquivo:
      arquivo.write('Conteúdo novo.')
  ```

- ### **'a'** (Escrita ao Final)
  Abre o arquivo para escrita e adiciona o conteúdo ao final, sem sobrescrever o que já existe.
  ```python
  with open('arquivo.txt', 'a') as arquivo:
      arquivo.write('Conteúdo adicional.')
  ```

- ### **'b'** (Binário)
  Abre o arquivo em modo binário. Esse modo é geralmente usado para manipular arquivos não textuais, como imagens ou arquivos de áudio.
  ```python
  with open('imagem.png', 'rb') as arquivo:
      conteudo_binario = arquivo.read()
  ```

- ### **'t'** (Texto)
  Modo padrão para abertura de arquivos de texto.
  ```python
  with open('arquivo.txt', 'rt') as arquivo:
      conteudo = arquivo.read()
  ```

- ### **'+'** (Leitura e Escrita)
  Permite tanto a leitura quanto a escrita em um arquivo.
  ```python
  with open('arquivo.txt', 'r+') as arquivo:
      conteudo = arquivo.read()
      arquivo.write('Novo conteúdo após leitura.')
  ```

- ### **Abrir e Fechar Arquivos**
  O `open()` é usado para abrir arquivos, e o `with` é recomendado, pois fecha o arquivo automaticamente.
  ```python
  with open('arquivo.txt', 'r') as arquivo:
      conteudo = arquivo.read()
  # Arquivo fechado automaticamente ao sair do bloco `with`
  ```

## Métodos
- **write**: Escreve uma string no arquivo.
- **read**: Lê o conteúdo inteiro do arquivo e retorna uma string.
- **writelines**: Escreve uma lista de strings no arquivo. Cada item da lista é uma linha.
- **seek**: Move o cursor de leitura/escrita para uma posição específica no arquivo.
- **readline**: Lê uma linha do arquivo por vez. Ideal para arquivos grandes ou para processar linha a linha.
- **readlines**: Lê todas as linhas do arquivo e retorna uma lista de strings, onde cada linha é um item da lista.

## Encoding

- É o conjunto de regras que define a representação dos caracteres em um formato específico de forma eficiente, variando de sistema operacional. Alguns exemplos utilizados:
  - UTF-8
  - ISO-8859
  - ASCII
  - Unicode
  - UTF-16
  ```python
  with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:
      conteudo = arquivo.read()
  # Arquivo fechado automaticamente ao sair do bloco `with`
  ```

## Biblioteca OS

- A biblioteca `os` fornece uma maneira simples de usar funcionalidades dependentes do sistema operacional. Para o uso do context manager, podemos usar os seguintes métodos:
  - **Remover Arquivo**
    ```python
    import os
    os.remove('arquivo.txt')
    os.unlink('arquivo.txt')
    ```
  - **Renomear Arquivo**
    ```python
    import os
    os.rename('arquivo.txt', 'novo_nome.txt')
    ```

# Criando Arquivos com Classes

Pode-se implementar seus próprios context managers implementando os métodos especiais `__enter__` e `__exit__`, utilizando o conceito de *duck typing*. O Python não se preocupa com o tipo do objeto, mas sim se ele possui os métodos necessários para funcionar.

## Duck Typing

> "Se algo caminha como um pato, nada como um pato e grasna como um pato, então deve ser um pato."

Ou seja, não importa o que seja, desde que se comporte como o esperado.

### Implementação de um Context Manager

Para criar um context manager, deve-se implementar os métodos `__enter__` e `__exit__`. O método `__exit__` recebe a classe de exceção e o traceback. Se ele retornar `True`, a exceção no bloco `with` será suprimida.

```python
class MeuContextManager:
    def __enter__(self):
        print("Entrando no bloco com.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"Exceção capturada: {exc_value}")
        print("Saindo do bloco com.")
        return True  # Suprime a exceção

with MeuContextManager():
    print("Dentro do bloco.")
    raise ValueError("Ocorreu um erro.")  # A exceção será suprimida
```

Essa abordagem garante limpeza de recursos, controle de exceções e retorno de valores.

# Context Manager com a Biblioteca `contextlib`

É possível criar um context manager utilizando funções decoradas e `generator` com a biblioteca `contextlib`, permitindo tratamento de erros e garantindo que o arquivo será sempre aberto e fechado corretamente.

```python
from contextlib import contextmanager

@contextmanager
def meu_context_manager(caminho_arquivo, modo):
    try:
        arquivo = open(caminho_arquivo, modo, encoding='utf-8')
        yield arquivo
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        arquivo.close()
```

Esse método é ideal porque o `finally` sempre será executado, garantindo o fechamento correto do arquivo.

