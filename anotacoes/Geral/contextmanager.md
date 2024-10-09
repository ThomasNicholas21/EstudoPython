# Criando arquivos com Python
- Neste usamos a função open para abrir um arquivo Python.

## Context Manager - with
- Utilizando o **_with_** ao inicializar alguma método em Python para leitura de arquivo, o mesmo irá abri-lo, executa-lo e irá fecha-lo.
    ```Python
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

- ### **'a'** (Escrita ao final)
Abre o arquivo para escrita e adiciona o conteúdo ao final, sem sobrescrever o que já existe.
```python
with open('arquivo.txt', 'a') as arquivo:
    arquivo.write('Conteúdo adicional.')
```

- ### **'b'** (Binário)
Abre o arquivo em modo binário. Esse modo é geralmente usado para manipular arquivos não-textuais, como imagens ou arquivos de áudio.
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
- **writeline**: Escreve uma lista de strings no arquivo. Cada item da lista é uma linha.
- **seek**: Move o cursor de leitura/escrita para uma posição específica no arquivo.
- **readline**: Lê uma linha do arquivo por vez. Ideal para arquivos grandes ou para processar linha a linha.
- **readlines**: Lê todas as linhas do arquivo e retorna uma lista de strings, onde cada linha é um item da lista.


## Enconding
- É o conjunto de regras que define a representação em um formato específico de forma efieciente, variando de sistema operacional. Alguns exemplos utilizados:
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
- O mesmo fornece uma menira simples de usar funcionalidades que são dependentes de sistema operacional. Para o uso do context manager, podemos usar os seguintes módulos:
    - Método: ***os.unlink*** ou ***os.remove***
    ```python
    import os

    os.remove('arquivo.txt')
    os.unlink('arquivv.txt')
    ```
    - Método: ***os.rename***
    ```python
    import os
    
    os.rename('arquivo.txt. novo_nome.txt')
    ```

# Criando arquivo com Classes
Pode-se implementar seus próprios protocolos apenas implementando os métodos especiais, sendo chamado de duck typing. Um conceito relacionado a tipagem dinâmica, onde o Python não está interessado no tipo (srt, int, float, etc.), mas se alguns métodos existem no seu objeto para que ele funcione.

## Duck Typing
Quando vejp um passáro que caminha como um pato, nada como um pato e grasna como um pato, eu chamo aquele passáro de pato. Ou seja, não se sabe o que é, porém parece um pato. 

- __context manager__
    - Para criar deve-se implementar os métodos '__enter__' e '__exit__'. O método '__exit__' recebera a classe de exceção e o traceback, se ele retornar True, exceção no __with__ será suprimida. *Exemplo*:
    ```Python
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
    - O mesmo garante limpeza de recursos, controle de excções e reotrne de valores.

# Context Manger com a lib contextlib
É possível criar um context manager com funções decorados e generetor utilizando a lib contextlib, podendo tratar erros e sempre abrir e fechar o arquivo. *Exemplo*:
   ```Python
    from contextlib import contexmanager

    def MyContextManager(caminho_arquivo, modo):
        try: # Trata excções
            arquivo = open(caminho_arquivo, modo, enconding='utf8')
            arquivo.open()
        except Exception as e:
            print('Trata excções')
        finally: # ideal pois sempre vai ser executado
            arquivo.close()
    ```