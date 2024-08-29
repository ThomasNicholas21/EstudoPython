# Revisão de estrutura de controle 💻
## Manipulação de String
- ## Fatiamento de String
    - **`string[start:stop:step]`**: Permite extrair partes de uma string.
        - **`start`**: Posição inicial (inclusiva, padrão é 0).
        - **`stop`**: Posição final (exclusiva, padrão é o final da string).
        - **`step`**: Passo entre os índices (padrão é 1).
        ```python
        texto = "Hello, World!"
        print(texto[0:5])    # Saída: Hello
        print(texto[7:12])   # Saída: World
        print(texto[::2])    # Saída: Hlo ol!
        print(texto[::-1])   # Saída: !dlroW ,olleH
        ```
    - **`Obersavação`**: Mais exemplos de Fatiamento de String ["clique aqui""](https://github.com/ThomasNicholas21/BootCampVivo/blob/master/estrutura_de_controle/manipulacao_string/fatiamento_strings.py)
- ## Interpolação de Variáveis
    - `%` - Versão Antiga
        - Utiliza o operador `%` para inserir variáveis dentro de strings.
            ```python
            nome = "Alice"
            idade = 30
            print("Nome: %s, Idade: %d" % (nome, idade))
            # Saída: Nome: Alice, Idade: 30
            ```

    - `format` - Especifica de Forma Automática
        - Usa o método `str.format()` para substituir os placeholders `{}` pela ordem dos argumentos fornecidos.
            ```python
            nome = "Bob"
            idade = 25
            print("Nome: {}, Idade: {}".format(nome, idade))
            # Saída: Nome: Bob, Idade: 25
            ```

    - `format` - Especifica de Forma Manual
        - Usa índices numéricos para especificar a ordem dos argumentos nos placeholders `{}`.
            ```python
            nome = "Carol"
            idade = 28
            print("Nome: {0}, Idade: {1}".format(nome, idade))
            # Saída: Nome: Carol, Idade: 28
            print("Idade: {1}, Nome: {0}".format(nome, idade))
            # Saída: Idade: 28, Nome: Carol
            ```

    - `format` - Especifica de Forma Lógica
        - Usa nomes de variáveis nos placeholders `{}` que correspondem aos argumentos nomeados fornecidos.
            ```python
            print("Nome: {nome}, Idade: {idade}".format(nome="Dave", idade=35))
            # Saída: Nome: Dave, Idade: 35
            ```

    - `format` - Desempacotando Dicionário
        - Usa a sintaxe `**` para desempacotar um dicionário e substituir os placeholders `{}` pelos valores correspondentes.
            ```python
            pessoa = {"nome": "Eve", "idade": 22}
            print("Nome: {nome}, Idade: {idade}".format(**pessoa))
            # Saída: Nome: Eve, Idade: 22
            ```

    - `f-strings`
        - Utiliza a sintaxe `f"{variável}"` para inserir variáveis diretamente dentro de strings. Disponível a partir do Python 3.6.
            ```python
            nome = "Frank"
            idade = 40
            print(f"Nome: {nome}, Idade: {idade}")
            # Saída: Nome: Frank, Idade: 40
            ```
    - **`Observação`**: Mais exemplos de Interpolação de Variáveis ["clique aqui""](https://github.com/ThomasNicholas21/BootCampVivo/blob/master/estrutura_de_controle/manipulacao_string/interpolacao_variaveis.py)

- ## Métodos para String
    - **`string.upper()`**: Converte todos os caracteres para maiúsculo.
        ```python
        texto = "python"
        print(texto.upper())
        # Saída: PYTHON
        ```

    - **`string.lower()`**: Converte todos os caracteres para minúsculo.
        ```python
        texto = "PYTHON"
        print(texto.lower())
        # Saída: python
        ```

    - **`string.title()`**: Converte o primeiro caractere de cada palavra para maiúsculo e o restante para minúsculo.
        ```python
        texto = "programação em python"
        print(texto.title())
        # Saída: Programação Em Python
        ```

    - **`string.strip()`**: Remove espaços em branco no início e no fim da string.
        ```python
        texto = "  python  "
        print(texto.strip())
        # Saída: python
        ```

    - **`string.lstrip()`**: Remove espaços em branco à esquerda da string.
        ```python
        texto = "  python"
        print(texto.lstrip())
        # Saída: python
        ```

    - **`string.rstrip()`**: Remove espaços em branco à direita da string.
        ```python
        texto = "python  "
        print(texto.rstrip())
        # Saída: python
        ```

    - **`string.center()`**: Alinha a string no centro, preenchendo com o caractere especificado até atingir o comprimento total desejado.
        ```python
        texto = "python"
        print(texto.center(10))
        # Saída: '  python  '
        print(texto.center(10, '-'))
        # Saída: --python--
        ```

    - **`string.split(sep, maxsplit)`**: Divide a string em uma lista com base no separador especificado. O `maxsplit` é opcional e define o número máximo de divisões.
        ```python
        texto = "python é divertido"
        print(texto.split())
        # Saída: ['python', 'é', 'divertido']
        print(texto.split(' ', 1))
        # Saída: ['python', 'é divertido']
        ```

    - **`'item'.join(string)`**: Junta os caracteres da string com o item especificado.
        ```python
        texto = "python"
        print('-'.join(texto))
        # Saída: p-y-t-h-o-n
        ```

    - **`string.replace(old, new, count)`**: Substitui todas as ocorrências da substring `old` por `new`. O argumento `count` é opcional e limita o número de substituições.
        ```python
        texto = "python é divertido"
        print(texto.replace("python", "programação"))
        # Saída: programação é divertido
        ```

    - **`string.startswith(prefix)`**: Verifica se a string começa com o prefixo especificado.
        ```python
        texto = "python é divertido"
        print(texto.startswith("python"))
        # Saída: True
        ```

    - **`string.endswith(suffix)`**: Verifica se a string termina com o sufixo especificado.
        ```python
        texto = "python é divertido"
        print(texto.endswith("divertido"))
        # Saída: True
        ```

    - **`string.find(sub)`**: Retorna o índice da primeira ocorrência da substring `sub`. Retorna -1 se a substring não for encontrada.
        ```python
        texto = "python é divertido"
        print(texto.find("divertido"))
        # Saída: 12
        ```

    - **`string.count(sub)`**: Conta quantas vezes a substring `sub` aparece na string.
        ```python
        texto = "python é divertido, python é fácil"
        print(texto.count("python"))
        # Saída: 2
        ```

    - **`string.zfill(width)`**: Preenche a string com zeros à esquerda até atingir o comprimento especificado.
        ```python
        texto = "42"
        print(texto.zfill(5))
        # Saída: 00042
        ```

    - **`string.isdigit()`**: Verifica se todos os caracteres na string são dígitos.
        ```python
        texto = "12345"
        print(texto.isdigit())
        # Saída: True
        ```

    - **`string.isalpha()`**: Verifica se todos os caracteres na string são letras.
        ```python
        texto = "python"
        print(texto.isalpha())
        # Saída: True
        ```
    - **`Observação`**: Mais exemplos de Métodos para String ["clique aqui""](https://github.com/ThomasNicholas21/BootCampVivo/blob/master/estrutura_de_controle/manipulacao_string/metodo_string.py)