# Pragramação Orientada a Objetos (POO)
Paradigma de programação é um estilo de programação de como solucionar problemas através do código. O paradigma de programação orientada a objetos faz a estruturação do código abstraindo problemas em objetos do mundo real, facilitando o entendimento do código e tornando-o mais flexível e modular.

## Classes e Objetos
- **```Classes```**
    - É o que define as características e comportamentos de um objeto, porém não é possível utilizar diretamente, ou seja, é algo abstrato. Por convenção é utilizado o PascalCase para nomear uma classe. A classe permite criar atributos, que seriam os dados dessa classe, e métodos, que são as ações que a classe possibilita.
- **```Objetos```**
    - O objeto instanciado por uma classe pode utilizar as características e comportamentos que foram definidos na classe.

Exemplo:
```python
class Calculadora:
    def somar(self, a, b):
        return a + b

calc = Calculadora()
resultado = calc.somar(3, 4)
print(resultado)  # 7
```

## Contrutores e Destrutores
- **```Método Contrutor```**
    - Inicializa de forma automática os atributos do objeto, chamado quando uma nova instância da classe é criada, sendo chamado de: ```__init__ ```
    Exemplo:
    ```python
    class MinhaClasse:
        def __init__(self, parametros):
            # Inicialização dos atributos
            self.atributo1 = valor1
            self.atributo2 = valor2
    ```
- **```Método Destrutor```**
    - Ele é chamado para realizar a destruição de um objeto, ou seja, para remover o objeto da memória. Ele é menos utilizado em Python, pois a linguagem possui um recurso de coletor de lixo, porém aquele que não é removido o método se torna útil, como por exemplo: conexões de rede ou recursos externos. Sendo representado por: ```__del__```.

    Exemplo:
    ```python
    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade
            print(f'{self.nome} foi criado.')

        def __del__(self):
            print(f'{self.nome} está sendo destruído.')git s

    # Criando uma instância da classe Pessoa
    pessoa1 = Pessoa("João", 30)

    # Deletando a instância explicitamente
    del pessoa1
    ```

## O que é *self*
- self é a instância da classe, ou seja, é uma referênciada classe ao próprio objeto que será manipulado.

## __dict__ e vars
- São métodos que transformam os atributos de um objeto em um dicionário.
    ```Python
    class Carro:
        def __init__(self, marca, portas):
            self.marca = marca
            self.portas = portas

    carro1 = Carro('Ford', 4)
    carro1.__dict__  # Transforma o objeto em dicionário
    vars(dict)       # Transforma o objeto em dicionário
    ```

## Método de importação de dados para uma classe
- É possível desempacotar um dicionário em uma instância de classe, permitindo que o objeto receba seus atributos de forma automática.
    ```Python
    class Carro:
        def __init__(self, marca, portas):
            self.marca = marca
            self.portas = portas

    carro = {'marca': 'Ford', 'portas': 4}
    carro1 = Carro(**carro)
    
    ```
