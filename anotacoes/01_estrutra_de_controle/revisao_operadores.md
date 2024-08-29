# Revisão de estrutura de controle 💻
## Indentação
- **`Indentação`**: O objetivo é manter o código fonte limpo, legível e manutenível. Em Python, a indentação é obrigatória e indica blocos de código.
    ```python
    if x > 0:
        print("x é positivo")
    ```
- **`Interpretador`**: Python consegue determinar onde o bloco inicia e onde ele termina através da indentação. Cada nível de indentação geralmente consiste em 4 espaços.
    ```python
    for i in range(5):
        if i % 2 == 0:
            print(f"{i} é par")
    ```
    
## Operadores
- ### Operadores de identificação
    - **`is`**: Verifica se duas variáveis apontam para o mesmo objeto na memória.
    ```python
    a = [1, 2, 3]
    b = a
    c = a[:]
    print(a is b)  # True
    print(a is c)  # False
    ```
    - **`is not`**: Verifica se duas variáveis não apontam para o mesmo objeto na memória.
    ```python
    print(a is not c)  # True
    ```
    - **`Observação`**: Mais exemplos de Operadores de identificação ["clique aqui""](https://github.com/ThomasNicholas21/BootCampVivo/blob/master/estrutura_de_controle/operadores/oepradores_identidadae.py)

- ### Operadores Aritiméticos
    - **`+`**: Soma.
    ```python
    print(2 + 3)  # 5
    ```
    - **`-`**: Subtração.
    ```python
    print(5 - 2)  # 3
    ```
    - **`*`**: Multiplicação.
    ```python
    print(3 * 4)  # 12
    ```
    - **`/`**: Divisão.
    ```python
    print(10 / 2)  # 5.0
    ```
    - **`//`**: Divisão inteira.
    ```python
    print(10 // 3)  # 3
    ```
    - **`%`**: Módulo (resto da divisão).
    ```python
    print(10 % 3)  # 1
    ```
    - **`**`**: Exponenciação.
    ```python
    print(2 ** 3)  # 8
    ```
    - **`Observação`**: Mais exemplos de Operadores Aritiméticos ["clique aqui""](https://github.com/ThomasNicholas21/BootCampVivo/blob/master/estrutura_de_controle/operadores/oepradores_identidadae.py)
- ### Operadores de Associação
    - **`in`**: Verifica se um valor está presente em uma sequência.
    ```python
    print('a' in 'banana')  # True
    ```
    - **`not in`**: Verifica se um valor não está presente em uma sequência.
    ```python
    print('x' not in 'banana')  # True
    ```
    - **`Observação`**: Mais exemplos de Operadores de Associação ["clique aqui""](https://github.com/ThomasNicholas21/BootCampVivo/blob/master/estrutura_de_controle/operadores/operadores_associcao.py)
- ### Operadores de Atribuição
    - **`=`**: Atribuição de valor.
    ```python
    x = 5
    ```
    - **`+=`**: Adição e atribuição.
    ```python
    x += 3  # x agora é 8
    ```
    - **`-=`**: Subtração e atribuição.
    ```python
    x -= 2  # x agora é 6
    ```
    - **`*=`**: Multiplicação e atribuição.
    ```python
    x *= 4  # x agora é 24
    ```
    - **`/=`**: Divisão e atribuição.
    ```python
    x /= 3  # x agora é 8.0
    ```
    - **`//=`**: Divisão inteira e atribuição.
    ```python
    x //= 2  # x agora é 4.0
    ```
    - **`%=`**: Módulo e atribuição.
    ```python
    x %= 3  # x agora é 1.0
    ```
    - **`**=`**: Exponenciação e atribuição.
    ```python
    x **= 3  # x agora é 1.0
    ```
    - **`Observação`**: Mais exemplos de Operadores de Atribuição ["clique aqui""](https://github.com/ThomasNicholas21/BootCampVivo/blob/master/estrutura_de_controle/operadores/operadores_atribuicao.py)
- ### Operadores de Comparação
    - **`==`**: Igualdade.
    ```python
    print(3 == 3)  # True
    ```
    - **`!=`**: Diferença.
    ```python
    print(3 != 2)  # True
    ```
    - **`>`**: Maior que.
    ```python
    print(5 > 3)  # True
    ```
    - **`>=`**: Maior ou igual.
    ```python
    print(3 >= 3)  # True
    ```
    - **`<`**: Menor que.
    ```python
    print(2 < 3)  # True
    ```
    - **`<=`**: Menor ou igual.
    ```python
    print(3 <= 3)  # True
    ```
    - **`Observação`**: Mais exemplos de Operadores de Comparação ["clique aqui""](https://github.com/ThomasNicholas21/BootCampVivo/blob/master/estrutura_de_controle/operadores/operadores_comparacao.py)
- ### Operadores Lógicos
    - **`and`**: Retorna `True` se ambas as expressões forem verdadeiras.
    ```python
    print(True and False)  # False
    ```
    - **`or`**: Retorna `True` se pelo menos uma das expressões for verdadeira.
    ```python
    print(True or False)  # True
    ```
    - **`not`**: Inverte o valor lógico.
    ```python
    print(not True)  # False
    ```
    - **`Observação`**: Mais exemplos de Operadores Lógicos ["clique aqui""](https://github.com/ThomasNicholas21/BootCampVivo/blob/master/estrutura_de_controle/operadores/operadores_logicos.py)