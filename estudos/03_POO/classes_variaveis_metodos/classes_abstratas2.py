# Estudand classes abstratas

# criando log utilizando abstra;áo
from abc import ABC, abstractmethod

class Log(ABC): # Não pode ser instânciado

    @abstractmethod
    def _log(self, msg): # Cria assinatura
        pass
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_sucesso(self, msg):
        return self._log(f'Sucess: {msg}')
    
# class LogFIleMixin(Log):
#     def _log(self, msg): 
#         mensagem = f'{msg} ({self.__class__.__name__})'
#         with open(LOG_FILE, 'a') as arquivo:
#             arquivo.write(mensagem)
#             arquivo.write('\n')

class LogPrintMixin(Log): 
    def _log(self, msg): 
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__': 
    log1 = LogPrintMixin()
    log1.log_sucesso('Método abstrato')