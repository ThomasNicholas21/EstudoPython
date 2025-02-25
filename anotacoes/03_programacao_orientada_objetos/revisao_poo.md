# Programação Orientada a Objetos (POO)
Paradigma de programação é um estilo de programação de como solucionar problemas através do código. O paradigma de programação orientada a objetos faz a estruturação do código abstraindo problemas em objetos do mundo real, facilitando o entendimento do código e tornando-o mais flexível e modular.

## Classes e Objetos
- **```Classes```**
    - É o que define as características e comportamentos de um objeto, porém não é possível utilizar diretamente, ou seja, é algo abstrato.
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

## Construtores e Destrutores
- **```Método Construtor```**
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
            print(f'{self.nome} está sendo destruído.')

    # Criando uma instância da classe Pessoa
    pessoa1 = Pessoa("João", 30)

    # Deletando a instância explicitamente
    del pessoa1
    ```

## Herança
- **O que é?**
    - Na programação orientada a objetos, herança é a capacidade de uma classe filha herdar as características e comportamentos da classe pai.
- **Vantagens:**
    - Faz a reutilização do código, para que não seja necessário repetir. Além disso, permite adicionar mais recursos a uma classe sem modificá-la.
    - É transitiva, caso uma classe B herde da classe A, todas as subclasses de B herdarão de forma automática da classe A, ou seja, caso a classe B tenha como filha a classe C, essa classe será neta da classe A herdando suas características.
        - **Obs:** Sempre verificar a complexidade da herança das classes, pois caso a família seja grande, uma pequena alteração irá refletir em toda a família.
## **Herança Simples**
- Quando uma classe filha herda apenas uma classe pai, essa é chamada de herança simples
```python
class A:
    pass
class B(A): # Filha da classe A
    pass
```
## **Herança Múltipla**
- Quando uma classe filha herda de várias classes pai, ela é chamada de herança múltipla.
```python
class A:
    pass
class B:
    pass
class C(A, B): # Herda características da classe A e B
    pass
```

## Polimorfismo
- **O que é?**
    - Na programação, polimorfismo significa o mesmo nome de função sendo usado para tipos diferentes, ou seja, ele possui comportamentos diferentes. Como por exemplo a função **len**:
    ```Python
    len('Python')
    len([10, 5, 11])
    ```
    O mesmo recebe objetos diferentes, e para cada objeto ele se comporta de uma maneira.
- **Polimorfismo e Herança:**
    - Utilizado quando o método herdado da classe pai não se encaixa perfeitamente na classe filha.
    ```Python
    class Animal:
        def __init__(self, nome):
            self.nome = nome

        def falar(self):
            raise NotImplementedError("Subclasses devem implementar o método 'falar'.")

    class Cachorro(Animal):
        def falar(self):
            return f"{self.nome} diz: Au au!"

    class Gato(Animal):
        def falar(self):
            return f"{self.nome} diz: Miau!"

    # Função que demonstra o polimorfismo
    def fazer_animal_falar(animal):
        print(animal.falar())

    # Criando instâncias das subclasses
    cachorro = Cachorro("Rex")
    gato = Gato("Mingau")
    
    # Usando o polimorfismo para fazer os animais "falarem"
    fazer_animal_falar(cachorro)
    fazer_animal_falar(gato)
    ```

### 👉 [Mais exemplos e atividades](https://github.com/ThomasNicholas21/EstudoPython/tree/master/estudos/03_POO)
