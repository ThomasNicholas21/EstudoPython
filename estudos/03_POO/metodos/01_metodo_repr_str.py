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
    
loca1 = Localizacao(123, 321)
loca2 = Localizacao(987, 789)
# Método __str__ chamado primeiro
print(loca1) 
print(loca2)
# Como ver o método __repr__
print(f'{loca1!r}')
print(f'{loca2!r}')
# ou
print(repr(loca1), repr(loca2))