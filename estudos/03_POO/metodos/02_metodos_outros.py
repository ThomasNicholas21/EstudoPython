# __repr__(self) - str   -- Método mais importante, pois indica como
# o opbjeto será remontado, ou seja, sinaliza como o objeto deve ser criado.
# __str__(self) - str    -- Método que representa a string do objeto

class Localizacao:
    def __init__(self, latitude, longitude) -> None:
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self) -> str:
        return f'({self.latitude}, {self.longitude})'
    
    def __repr__(self) -> str: # Como o método é montado
        return f'{self.__class__.__name__}(x:{self.longitude!r}, y:{self.longitude!r})'

    def __add__(self, other_object): # Método __add__ faz a soma de dois objetos
        nova_latitude = self.latitude + other_object.latitude
        nova_longitude = self.longitude + other_object.longitude
        return Localizacao(nova_latitude, nova_longitude) # Método de fabrica
    
if __name__ == '__main__':   
    loca1 = Localizacao(123, 321)
    loca2 = Localizacao(987, 789)
    # Método __add__ faz a soma de dois objetos
    loca3 = loca1 + loca2
    print(repr(loca3), loca3)
    # para utilizar outros métodos, necessário ler a documentação e entender a lógica do código
    
    