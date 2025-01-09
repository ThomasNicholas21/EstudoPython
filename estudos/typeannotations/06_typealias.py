# Type alias é uma forma de atribuir a tipagem em uma variável


ListaStrings = list[str]
ListaTuples = list[tuple]
ListaInteiros = list[int]
ListaFloat = list[float]
ListaDeListas = list[list[int | float]]
ListaDicionarios = list[dict]

lista1: ListaStrings = ['a', 'b', 'c', 'd']
lista2: ListaTuples = [(1, 2), (3, 2)]
lista3: ListaInteiros = [1, 2, 3, 4]
lista4: ListaFloat = [1.2, 2.3, 4.2]
lista5: ListaDeListas = [[1, 3.4], [1, 3], [2.5, 1]]
lista6: ListaDicionarios = [{'a': 1}, {'b': 2}]
