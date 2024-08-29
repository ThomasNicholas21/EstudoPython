# Revisão de estrutura de controle 💻
## Estrutura Condicional
- **`if`**: Executa um bloco de código se a condição for verdadeira.
    ```python
    x = 10
    if x > 5:
        print("x é maior que 5")  # Saída: x é maior que 5
    ```
- **`if-else`**: Executa um bloco de código se a condição for verdadeira, senão executa outro bloco de código.
    ```python
    x = 3
    if x > 5:
        print("x é maior que 5")
    else:
        print("x é menor ou igual a 5")  # Saída: x é menor ou igual a 5
    ```
- **`elif`**: Verifica múltiplas condições. Se a condição `if` for falsa, verifica a condição `elif`.
    ```python
    x = 5
    if x > 5:
        print("x é maior que 5")
    elif x == 5:
        print("x é igual a 5")  # Saída: x é igual a 5
    else:
        print("x é menor que 5")
    ```

- **`if`** aninhado
    - São condicionais dentro de condicionais, permitindo verificar múltiplas condições em níveis diferentes.
        ```python
        x = 10
        if x > 5:
            print("x é maior que 5")
            if x > 8:
                print("x é também maior que 8")  # Saída: x é maior que 5
                                                #         x é também maior que 8
        ```

- **`if`** ternário
    - Condição em uma única linha. Avalia a condição e retorna um valor com base no resultado.
        ```python
        x = 10
        resultado = "Maior que 5" if x > 5 else "Menor ou igual a 5"
        #"retorno da primeira condição" if condição else "retorno da segunda"
        print(resultado)  # Saída: Maior que 5
        ```

- **`Observação`**: Mais exemplos de Estrutura Condicional ["clique aqui""](https://github.com/ThomasNicholas21/BootCampVivo/blob/master/estrutura_de_controle/condicional_repeticao/estrutura_condicionais.py)