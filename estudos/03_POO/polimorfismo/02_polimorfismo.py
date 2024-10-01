# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅
from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ... # Isso se chama Type anotation, aonde indica o que o método deve retornar, tanto para desenvolvedores, quanto para o VsCode
    # caso os métodos das subclasses não retornarem um bool, irá quebrar um princípio da susbstituição de liskov SO 'L' ID

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando - ', self.mensagem)
        return True

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('Email: enviando - ', self.mensagem)
        return True
    
def notificacao(notificacao: Notificacao): # Fazer isso faz com que realize uma tipagem do parâmetro, fazendo com que ele receba os métodos
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação não enviada')

if __name__ == '__main__':
    notif_email = NotificacaoEmail('Teste notificação email')
    notif_sms = NotificacaoSMS('Teste ntoficação SMS')
    # polimorfismo
    notificacao(notif_email)
    notificacao(notif_sms)