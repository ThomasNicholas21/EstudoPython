# criando log utilizando abstra;áo
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'
class Log:
    def _log(self, msg): # Assinatura
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_sucesso(self, msg):
        return self._log(f'Sucess: {msg}')
    
class LogFIleMixin(Log): # Mixin é uma convenção que indica que o mesmo não será da familia do objeto, pois é uma classe que adiciona funcionalidade em outras classes
    def _log(self, msg): # Assinatura
        mensagem = f'{msg} ({self.__class__.__name__})'
        with open(LOG_FILE, 'a') as arquivo: # Modo 'a'de append, não irá sobrescrever os arquivos
            arquivo.write(mensagem)
            arquivo.write('\n')

class LogPrintMixin(Log): 
    def _log(self, msg): # Assinatura
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__': # Irá executar apenas no arquivo __main__
    l1 = LogFIleMixin()
    l2 = LogPrintMixin()
    l1.log_error('Mensagem de erro')
    l1.log_sucesso('Mensagem de sucesso')
    l2.log_error('Mensagem de erro')
    l2.log_sucesso('Mensagem de sucesso')