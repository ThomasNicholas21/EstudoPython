# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será
# suprimidas.
import json

class MyOpenCliente:
    def __init__(self, arquivo, modo) -> None:
        self.arquivo = arquivo
        self.modo = modo
        self._arquivo_abrir = None

    def __enter__(self): # Responsável por abrir o arquivo
        print('Inicializando abertura do arquivo')
        self._arquivo_abrir = open(self.arquivo, self.modo, encoding='utf8')
        return self._arquivo_abrir

    # Estudando como tratar erro
    def __exit__(self, class_exception_, exception_, traceback_): # Responsável por fechar o arquivo
        print('Fechando o arquivo')
        # é possível tratar erros pelo método exit
        print(class_exception_)
        print(exception_)
        print(traceback_)
        
        # raise class_exception_(*exception_.args).with_traceback(traceback_)

        # raise class_exception_
    
        exception_.add_note('Adicionando nota sobre excção')

        self._arquivo_abrir.close()

        # return True # Forma de tratar excções


def cadastro_cliente(dicionario_cliente: dict):
    print('Iniciando cadastro de cliente.')
    nome = input('Nome: ')
    data_nascimento = input('Data de nascimento: ')
    cpf = input('CPF: ')
    dicionario_cliente.update({'Cliente': {'Nome': nome, 'Nascimento': data_nascimento, 'CPF': cpf}})
    return dicionario_cliente

def main():
    dicionario_cliente = {}
    cadastro_cliente(dicionario_cliente)
    with MyOpenCliente('D:/programação/EstudoPython/estudos/03_POO/context_manager/02/arquivo.json', 'w') as arquivo:
        if dicionario_cliente:
            json.dump(dicionario_cliente, arquivo, 123)

main()