# Revisão de estrutura de controle 💻

## Estrutura Match Case

- **`match`**: Define qual variável estará sendo analisada.
    ```python
    def execute_any(any: str):
        match any: 
            ...
    ```
- **`match-case`**: Ao definir cases, executa a variável definida no match. 
    ```python
    def execute_any(any: str):
        match any:
            case 'start':
                print('Starting')
            case 'stop':
                print('Stopping')
            case 'exit':
                print('Exiting')
    ```
- **`Variável _ `**: A variável `_` funciona como um "else" em match-case, caso não haja nenhum case compatível.
    ```python
    def command(command: str):
        match command:
            case 'start':
                print('Starting')
            case 'stop':
                print('Stopping')
            case 'exit':
                print('Exiting')
            case _:
                print('Unknown command')
    ```

## Structural Pattern Matching 🏗️

O Structural Pattern Matching permite combinar padrões mais complexos, como tipos de dados estruturados, listas, dicionários e até mesmo instâncias de classes.

### Exemplo com Listas

```python
match data:
    case [first, second]:
        print(f"Lista com dois elementos: {first}, {second}")
    case [first, *rest]:
        print(f"Primeiro elemento: {first}, restante: {rest}")
    case _:
        print("Lista vazia ou padrão desconhecido")
```

### Exemplo com Dicionários

```python
match person:
    case {"name": name, "age": age}:
        print(f"Nome: {name}, Idade: {age}")
    case _:
        print("Formato desconhecido")
```

### Exemplo com Objetos

```python
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

user = User("Alice", "admin")

match user:
    case User(name="Alice", role="admin"):
        print("Usuário administrador")
    case User(name=name, role=role):
        print(f"Usuário comum: {name}, Role: {role}")


# Revisão de estrutura de controle 💻

## Estrutura Match Case

- **`match`**: Define qual variável estará sendo analisada.
    ```python
    def execute_any(any: str):
        match any: 
            ...
    ```
- **`match-case`**: Ao definir cases, executa a variável definida no match. 
    ```python
    def execute_any(any: str):
        match any:
            case 'start':
                print('Starting')
            case 'stop':
                print('Stopping')
            case 'exit':
                print('Exiting')
    ```
- **`Variável _ `**: A variável `_` funciona como um "else" em match-case, caso não haja nenhum case compatível.
    ```python
    def command(command: str):
        match command:
            case 'start':
                print('Starting')
            case 'stop':
                print('Stopping')
            case 'exit':
                print('Exiting')
            case _:
                print('Unknown command')
    ```

## Structural Pattern Matching 🏗️

O Structural Pattern Matching permite combinar padrões mais complexos, como tipos de dados estruturados, listas, dicionários e até mesmo instâncias de classes.

### Exemplo com Listas

```python
match data:
    case [first, second]:
        print(f"Lista com dois elementos: {first}, {second}")
    case [first, *rest]:
        print(f"Primeiro elemento: {first}, restante: {rest}")
    case _:
        print("Lista vazia ou padrão desconhecido")
```

### Exemplo com Dicionários

```python
match person:
    case {"name": name, "age": age}:
        print(f"Nome: {name}, Idade: {age}")
    case _:
        print("Formato desconhecido")
```

### Exemplo com Objetos

```python
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

user = User("Alice", "admin")

match user:
    case User(name="Alice", role="admin"):
        print("Usuário administrador")
    case User(name=name, role=role):
        print(f"Usuário comum: {name}, Role: {role}")

```

**`Observação`**: Mais exemplos de Match Case ["clique aqui"](https://github.com/ThomasNicholas21/EstudoPython/tree/master/estudos/01_estrutura_de_controle/match_case)
