# criando log utilizando abstra;áo

class Log:
    def log(self, msg): # Assinatura
        raise NotImplementedError('Implemente o método log')
    
class LogFIleMixin(Log): # Mixin é uma convenção que indica que o mesmo não será da familia do objeto, pois é uma classe que adiciona funcionalidade em outras classes
    def log(self, msg): # Assinatura
        print(msg)


if __name__ == '__main__': # Irá executar apenas no arquivo __main__
    l = LogFIleMixin()
    l.log('Teste')