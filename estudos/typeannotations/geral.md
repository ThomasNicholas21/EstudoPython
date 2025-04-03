# Type Annotations em Python 🐍

## Por que usar Type Annotations? 🤔

O uso de **Type Annotations** em Python melhora a legibilidade e a manutenção do código, ajudando a prevenir erros comuns ao indicar os tipos de dados esperados. Isso é especialmente útil em projetos grandes, onde múltiplos desenvolvedores interagem com o código. Além disso, ferramentas como `mypy` e `flake8` podem ser utilizadas para verificar a coerência das tipagens.

---

## Sintaxe Básica

A anotação de tipos pode ser aplicada a variáveis da seguinte forma:

```python
string: str = 'Hello, World!'
inteiro: int = 42
ofloat: float = 3.14
boleano: bool = True
lista: list = [1, 2, 3]
dicionario: dict = {'chave': 'valor'}
conjunto: set = {1, 2, 3}
tupla: tuple = (1, 2, 3)
```

Caso tente redefinir a variável para um tipo diferente, o `mypy` pode apontar um erro:

```python
string = 123  # Erro detectado pelo mypy
```

---

## Type Annotations em Funções

Podemos especificar os tipos dos parâmetros e do valor retornado:

```python
def somar(x: float, y: int) -> float:
    return x + y

soma = somar(2.5, 3)
print(soma)  # 5.5
```

---

## Anotação para Listas e Dicionários

Python permite tipar listas e dicionários:

```python
lista_numeros: list[int] = [1, 2, 3, 4]
dicionario_pessoas: dict[str, int] = {'Alice': 25, 'Bob': 30}
```

Podemos também criar listas de dicionários:

```python
lista_dicionarios: list[dict[str, float]] = [{'peso': 70.5}, {'altura': 1.75}]
```

---

## Conjuntos e Tuplas Tipados

```python
conjunto_numeros: set[int] = {1, 2, 3}
tupla_valores: tuple[int, float, str] = (1, 2.5, 'Python')
```

---

## Criando Type Aliases

Se tivermos listas ou estruturas de dados repetitivas, podemos criar apelidos para simplificar:

```python
ListaStrings = list[str]
ListaInteiros = list[int]
ListaDicionarios = list[dict[str, int]]

nomes: ListaStrings = ['Alice', 'Bob', 'Charlie']
```

---

## Usando `Union` para Aceitar Múltiplos Tipos

O operador `|` permite definir múltiplos tipos aceitos:

```python
Numero = int | float

def dobrar(valor: Numero) -> Numero:
    return valor * 2

print(dobrar(10))   # 20
print(dobrar(5.5))  # 11.0
```

---

## Tipando Parâmetros Opcionais (`Optional`)

Se um argumento for opcional, podemos defini-lo com `None`:

```python
def somar(x: float, y: float | int | None = None) -> float:
    if y is not None:
        return x + y
    return x + x

print(somar(3))    # 6
print(somar(3, 4)) # 7
```

---

## Funções como Parâmetros (`Callable`)

Podemos definir que um parâmetro deve ser uma função:

```python
from collections.abc import Callable

SomaInteiros = Callable[[int, int], int]

def executar(func: SomaInteiros, a: int, b: int) -> int:
    return func(a, b)

def soma(a: int, b: int) -> int:
    return a + b

print(executar(soma, 2, 3))  # 5
```

---

## Tipos Genéricos (`TypeVar`)

Podemos usar `TypeVar` para tornar funções mais flexíveis:

```python
from typing import TypeVar

T = TypeVar('T')

def pegar_item(lista: list[T], indice: int) -> T:
    return lista[indice]

print(pegar_item([1, 2, 3], 1))  # 2
print(pegar_item(['a', 'b', 'c'], 1))  # 'b'
```

---

## Tipagem para Classes

Podemos utilizar classes como tipos:

```python
class Pessoa:
    def __init__(self, primeiro_nome: str, segundo_nome: str):
        self.primeiro_nome = primeiro_nome
        self.segundo_nome = segundo_nome

    @property
    def nome_completo(self) -> str:
        return f'{self.primeiro_nome} {self.segundo_nome}'

def obter_nome_completo(pessoa: Pessoa) -> str:
    return pessoa.nome_completo

p = Pessoa('João', 'Silva')
print(obter_nome_completo(p))  # 'João Silva'
```

---

## Conclusão 🎯

O uso de **Type Annotations** ajuda a escrever código mais seguro e legível, evitando erros antes da execução. Ferramentas como `mypy` podem ser usadas para garantir a consistência dos tipos. Aplicando essas boas práticas, você melhora a qualidade do código e facilita a colaboração em equipe!


