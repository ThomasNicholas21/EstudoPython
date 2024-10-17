# Estudo de metaclasse

class Meta(type): # cria a classe
    def __new__(msc, name, bases, dct): # Deve retornar a classe 
        print('METACLASS NEW')
        cls = super().__new__(msc, name, bases, dct)
        cls.attr = 123456

        # irá retornar erro caso a classe Pessoa não tenha o método ou caso não seja um método
        if 'falar'not in cls.__dict__ or not \
            callable(cls.__dict__['falar']): 
            print(cls.__dict__) # Mostra o que foi definido na classe
            raise NotImplementedError('Implemente Falar')
        
        return cls
    
    def __call__(self, *args, **kwargs): # cria e retorna a instância
        instancia = super().__call__(*args, **kwargs) 

        if 'name' not in instancia.__dict__:
            raise NotImplementedError('Atributo nome não atribuido')
        
        return instancia

class Pessoa(metaclass=Meta): # Instância de Meta
    def __new__(cls, *args, **kwargs): # Deve retornar o objeto instanciado
        print('NEW')
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self, nome):
        print('INIT')
        self.nome = nome
    
    def falar(self): # Método implementado
        print('Falando')

pessoa1 = Pessoa('Fulano') # instância da classe Pessoa
print(pessoa1.attr)
print(Pessoa.attr)