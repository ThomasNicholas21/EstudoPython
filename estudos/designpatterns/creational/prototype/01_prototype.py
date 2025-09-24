"""
- Client
- Prototype
- ConcretePrototype
- SubclassPrototype
"""
from __future__ import annotations
from copy import deepcopy


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name) -> None:
        self._name = name

    @name.deleter
    def name(self) -> None:
        del self._name

    @property
    def age(self) -> str:
        return self._age

    @age.setter
    def age(self, age) -> None:
        if age < 0:
            raise ValueError("A idade não pode ser negativa.")
        self._age = age

    @age.deleter
    def age(self) -> None:
        del self._age

    def __repr__(self) -> str:
        return f"Person(name='{self.name}', age={self.age})"

    def clone(self) -> Person:
        return deepcopy(self)


if __name__ == "__main__":
    pessoa = Person("Thomas", 25)
    pessoa.name = "Nicholas"
    print(pessoa)
    pessoa_1 = pessoa.clone()
    pessoa_1.name = "John"
    print(pessoa_1)
