# Revisão de estrutura de controle 💻
## Estrutura de Repetição
- ### `for` e `for-else`
    - **`for`**: Utilizado para iterar sobre uma sequência (como uma lista, tupla ou string).
        ```python
        for i in range(5):
            print(i)
        # Saída: 0, 1, 2, 3, 4
        ```
    - **`for-else`**: O bloco `else` é executado quando o loop é concluído normalmente, ou seja, não foi interrompido por um `break`, caso seja, o `else` não é executado.
        ```python
        for i in range(5):
            print(i)
        else:
            print("Loop concluído sem interrupção.")
        # Saída: 0, 1, 2, 3, 4
        #         Loop concluído sem interrupção.

        ```

- ### `while`
    - Utilizado para repetir um bloco de código enquanto a condição for verdadeira.
        ```python
        x = 0
        while x < 5:
            print(x)
            x += 1
        # Saída: 0, 1, 2, 3, 4
        ```
    - **`while-else`**:
    ```python
        x = 0
        while x < 5:
            print(x)
            x += 1
        else:
            print('Contagem concluída sem interreupção!')
        # Saída: 0, 1, 2, 3, 4
        #         Contagem concluída sem interreupção!
    ```
- ### `break`
    - Utilizado para interromper o loop imediatamente.
        ```python
        for i in range(5):
            if i == 3:
                break
            print(i)
        # Saída: 0, 1, 2
        ```

- ### `continue`
    - Utilizado para pular a iteração atual e continuar com a próxima.
        ```python
        for i in range(5):
            if i == 3:
                continue
            print(i)
        # Saída: 0, 1, 2, 4
        ```

- ### `pass`
    - Utilizado como um placeholder em um loop, função ou classe, indicando que nada deve ser feito.
        ```python
        for i in range(5):
            if i == 3:
                pass
            print(i)
        # Saída: 0, 1, 2, 3, 4
        ```

- ### Momentos Ideais para Uso
    - **`for`**: Ideal para iterar sobre elementos de uma sequência, quando você sabe antecipadamente quantas iterações são necessárias.
    - **`for-else`**: Útil quando você precisa executar um código após a conclusão do loop, mas apenas se o loop não foi interrompido.
    - **`while`**: Ideal quando você não sabe antecipadamente quantas iterações serão necessárias e a repetição depende de uma condição.
    - **`break`**: Útil para sair de um loop antes que todas as iterações sejam concluídas, geralmente usado dentro de uma condição.
    - **`continue`**: Útil para pular a iteração atual e continuar com a próxima, geralmente usado para ignorar certos casos dentro de um loop.
    - **`pass`**: Útil como um placeholder quando a sintaxe exige um comando, mas você não quer executar nenhuma ação no momento.

- **`Observação`**: Mais exemplos de Estrutura de Repetição ["clique aqui""](https://github.com/ThomasNicholas21/BootCampVivo/blob/master/estrutura_de_controle/condicional_repeticao/estrutura_repeticao.py)
