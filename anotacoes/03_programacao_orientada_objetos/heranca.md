## Herança
- **O que é?**
    - Na programação orientada a objeto, herança é a capacidade de uma classe filha herdar as características e comportamento da classe pai.
- **Vantagens:**
    - Faz a reutilização do código, para que não seja necessário repetir. Além disso, permite adicionar mais recursos a uma classe sem modificá-la.
    - É transitiva, caso uma classe B herde da classe A, todas as subclasses de B herdarão de forma automática da classe A, ou seja, caso a classe B tenha como filha a classe C, essa classe será neta da classe A herdando suas caractéristicas.
        - **Obs:** Sempre verificar a complexidade da herança das classe, pois caso a família seja grande, uma pequena alteração irá refletir em toda a família.

- **Como funciona?**
    - A classe principal que estende a outra, ou seja, a classe pai é chamada de super class, base class, parent class.
    - A classe filha é chamada de sub class, child class, derived class
    
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


### 👉 [Mais exemplos e atividades](https://github.com/ThomasNicholas21/EstudoPython/tree/master/estudos/03_POO/heranca)
