# Estrutura de Dados
# frozenset
- É uma coleção de dados desordenadas, porém imutável. Sendo ela uma representação de conjuntos matemáticos;
    ```Python
    meu_frozenset = frozenset([1, 2, 3])
    ```

# set

- ### O que é "set"
    - Uma coleção de dados que possui elementos unicos, ou seja, não possui elementos repitidos. Assim sendo, irá representar os conjuntos matemáticos. Dessa forma, não necessáriamente em ordem.

- ### Como se utilizar
    - Para utilizar __set__ em python, é necessário definir um objeto da seguinte maneira:
        ```Python
        conjunto = {1, 2, 3, 4}
        print(set([1, 2, 3]))
        ```
    - Conjunto é um objeto mutável, no qual permite alterar após sua criação.

# Métodos

### **union**
Realiza a união entre dois ou mais conjuntos.

```python
a = {1, 2, 3}
b = {3, 4, 5}
resultado = a.union(b)  # {1, 2, 3, 4, 5}
```

### **intersection**
Retorna a intersecção entre dois ou mais conjuntos.

```python
a = {1, 2, 3}
b = {2, 3, 4}
resultado = a.intersection(b)  # {2, 3}
```

### **difference**
Retorna a diferença entre dois conjuntos.

```python
a = {1, 2, 3}
b = {2, 3, 4}
resultado = a.difference(b)  # {1}
```

### **symmetric_difference**
Retorna os elementos que estão em um conjunto ou no outro, mas não em ambos.

```python
a = {1, 2, 3}
b = {2, 3, 4}
resultado = a.symmetric_difference(b)  # {1, 4}
```

### **issubset**
Verifica se um conjunto é subconjunto de outro.

```python
a = {1, 2}
b = {1, 2, 3}
resultado = a.issubset(b)  # True
```

### **issuperset**
Verifica se um conjunto é superconjunto de outro.

```python
a = {1, 2, 3}
b = {1, 2}
resultado = a.issuperset(b)  # True
```

### **isdisjoint**
Verifica se dois conjuntos são disjuntos (não possuem elementos em comum).

```python
a = {1, 2}
b = {3, 4}
resultado = a.isdisjoint(b)  # True
```

### **add**
Adiciona um elemento ao conjunto.

```python
a = {1, 2}
a.add(3)  # a = {1, 2, 3}
```

### **clear**
Remove todos os elementos do conjunto.

```python
a = {1, 2, 3}
a.clear()  # a = set()
```

### **copy**
Cria uma cópia rasa do conjunto.

```python
a = {1, 2, 3}
b = a.copy()  # b = {1, 2, 3}
```

### **discard**
Remove um elemento do conjunto, sem gerar erro caso o elemento não exista.

```python
a = {1, 2, 3}
a.discard(2)  # a = {1, 3}
```

### **pop**
Remove e retorna um elemento arbitrário do conjunto.

```python
a = {1, 2, 3}
elemento = a.pop()  # Remove o primeiro elemento (a ordem não é garantida)
```

### **remove**
Remove um elemento do conjunto, gerando erro caso o elemento não exista.

```python
a = {1, 2, 3}
a.remove(2)  # a = {1, 3}
```

### **len**
Retorna o tamanho do conjunto.

```python
a = {1, 2, 3}
tamanho = len(a)  # 3
```

### **in**
Verifica se um elemento está presente no conjunto.

```python
a = {1, 2, 3}
resultado = 2 in a  # True
```

