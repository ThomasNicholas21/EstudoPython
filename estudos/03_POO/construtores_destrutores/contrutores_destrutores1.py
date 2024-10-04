class Garrafa:
    def __init__(self, tamanho, cor, quebrada=False): # Inicializando classe com __init__
        self.tamanho = tamanho
        self.cor = cor
        self.quebrada = quebrada

    def __str__(self):
        return f'{self.__class__.__name__}:{[', '.join(f'{chave}:{valor}' for chave, valor in self.__dict__.items())]}'

    def colocar_agua(self):
        if self.quebrada:
            return print(f'{self.__class__.__name__} está quebrada e não pode ser enchida.')
        return print(f'{self.__class__.__name__} está sendo enchida.')

    def __del__(self): # Deletando os objetos não utilizados com __del__
        print(f'{self.__class__.__name__} está sendo destruida')

garrafa_stanley = Garrafa('2L', 'Azul', False)
print(garrafa_stanley)
garrafa_stanley.colocar_agua()
garrafa_falsificada = Garrafa('3L', 'Vermelha', True)
print(garrafa_falsificada)
garrafa_falsificada.colocar_agua()

