# Metaclasses
Metaclasses em Python são consideradas "fábricas de classes". Elas permitem a modificação do comportamento da criação de classes, uma vez que Python trata classes como objetos. Assim, quando uma classe é definida, na verdade, está sendo criado um objeto com base nessa definição.

Com metaclasses, é possível:
- **Modificar a criação de classes**: Interceptar a criação de uma classe e alterar sua estrutura.
- **Adicionar ou modificar métodos automaticamente**: Adicionar métodos ou alterar o comportamento de métodos de uma classe ao criá-la.
- **Alterar atributos de classe**: Modificar ou adicionar atributos ao criar a classe.
- **Validação de classes**: Realizar verificações durante a criação de uma classe para garantir que ela esteja de acordo com certas regras.
## O tipo de uma classe
Em Python, o tipo de uma classe é `type`. `type` é uma metaclasse embutida que é responsável por criar outras classes. Quando você define uma classe, o Python chama `type()` para criar a classe.

Exemplo:

```python
class MinhaClasse:
    pass

# Verificando o tipo de MinhaClasse
print(type(MinhaClasse))  # Saída: class 'type'

# Criando uma instância de MinhaClasse
obj = MinhaClasse()

# Verificando o tipo da instância
print(type(obj))  # Saída: __main__.MinhaClasse
```
Aqui, `MinhaClasse` é um objeto de `type`, e `obj` é um objeto de `MinhaClasse`.
## O que ocorre ao criar uma classe em Python?
Quando você cria uma classe em Python, os seguintes eventos ocorrem:
1. O método `__new__` da metaclasse é chamado para criar a nova classe.
2. O método `__init__` da metaclasse é chamado com os argumentos para inicializar a classe.
3. Finalmente, quando você cria uma instância da classe, o método `__call__` da metaclasse é invocado.

Esses métodos podem ser modificados para alterar a maneira como as classes são criadas.

Exemplo de metaclasse:
```python
class MinhaMetaClasse(type):
    def __new__(mcs, name, bases, dct):
        print(f"Criando classe {name}")
        return super().__new__(mcs, name, bases, dct)

class MinhaClasse(metaclass=MinhaMetaClasse):
    pass

# Criando uma instância
obj = MinhaClasse()
```
## Métodos importantes de uma metaclasse
- `__new__(mcs, name, bases, dct)` – Método responsável por criar a classe. `mcs` refere-se à metaclasse, `name` é o nome da classe, `bases` são as classes base (herança) e `dct` é o dicionário que contém os atributos da classe.
- `__init__(cls, name, bases, dct)` – Inicializa a classe recém-criada. `cls` refere-se à classe recém-criada, e os outros argumentos são os mesmos de `__new__`.
- `__call__(cls, *args, **kwargs)` – Responsável por criar e inicializar instâncias da classe. `cls` é a classe a ser instanciada, e `*args` e `**kwargs` são os argumentos passados à instância.
## Exemplo completo:
```python
class MinhaMetaClasse(type):
    def __new__(mcs, name, bases, dct):
        print(f"Criando a classe {name}")
        dct['novo_metodo'] = lambda self: "Novo método adicionado pela metaclasse"
        return super().__new__(mcs, name, bases, dct)
    
    def __call__(cls, *args, **kwargs):
        print(f"Criando uma instância da classe {cls.__name__}")
        return super().__call__(*args, **kwargs)

class MinhaClasse(metaclass=MinhaMetaClasse):
    def __init__(self, valor):
        self.valor = valor

# Criando uma instância
obj = MinhaClasse(10)

# Acessando o novo método adicionado pela metaclasse
print(obj.novo_metodo())
```