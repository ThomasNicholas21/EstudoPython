
# Tratamento de Erros em Python

Python oferece maneiras de lidar com erros e exceções, permitindo que o programa trate situações inesperadas sem quebrar.

## try e except

O bloco `try` é usado para envolver o código que pode gerar uma exceção. Quando ocorre um erro dentro do `try`, o controle é passado para o bloco `except`, onde o erro pode ser tratado.

### Exemplo:
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida.")
```

## Capturando Vários Erros

Você pode capturar diferentes tipos de erros em blocos `except` separados.

### Exemplo:
```python
try:
    lista = [1, 2, 3]
    print(lista[10])
except IndexError:
    print("Erro: índice fora do intervalo da lista.")
except ZeroDivisionError:
    print("Erro: divisão por zero.")
```

## Erros Comuns

Erros comuns que podem ser capturados e tratados:

- `ZeroDivisionError`: Divisão por zero.
- `IndexError`: Tentativa de acessar um índice inválido em uma lista.
- `KeyError`: Tentativa de acessar uma chave inexistente em um dicionário.
- `TypeError`: Operação com tipos incompatíveis.
- `ValueError`: Valor inadequado passado para uma função.

### Exemplo:
```python
try:
    num = int("texto")
except ValueError:
    print("Erro: não é possível converter texto em número.")
```

## Usando `else`

O bloco `else` é executado se nenhuma exceção for levantada no bloco `try`.

### Exemplo:
```python
try:
    num = 10 / 2
except ZeroDivisionError:
    print("Erro: divisão por zero.")
else:
    print("Divisão bem-sucedida!")
```

## `finally`

O bloco `finally` sempre é executado, independentemente se uma exceção ocorreu ou não. Ele é útil para liberar recursos, como arquivos abertos.

### Exemplo:
```python
try:
    arquivo = open('meu_arquivo.txt', 'r')
except FileNotFoundError:
    print("Erro: arquivo não encontrado.")
finally:
    print("Bloco 'finally' executado.")
```

## `raise`

O comando `raise` permite que você lance uma exceção manualmente. Isso é útil quando você deseja sinalizar um erro específico em seu código.

### Exemplo:
```python
def verificar_numero(num):
    if num < 0:
        raise ValueError("Número negativo não permitido.")
    return num

try:
    verificar_numero(-5)
except ValueError as e:
    print(f"Erro: {e}")
```


