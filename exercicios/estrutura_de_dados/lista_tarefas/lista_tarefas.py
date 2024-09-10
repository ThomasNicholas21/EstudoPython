# Lista de Tarefas
# Definição: realizar a listagem, desfaz uma ação e refazaz uma ação 


class lista_tarefas:
    def inserir_tarefa(self, valor, lista_tarefa):
        lista_tarefa.append(valor)

    def apaga_tarefa(self, valor, lista_tarefa, lista_lixeira):
        lista_lixeira.append(valor)
        lista_tarefa.remove(valor)

    def refaz_tarefa(self, valor, lista_tarefa, lista_lixeira):
        for item in lista_lixeira:
            if item == valor:
                lista_tarefa.append(item)

    def __str__(self):
        return f'{self.__name__.__class__}{'\n'.join([item for item in self.lista])}'

def listar(lista_tarefas):
    return print(lista_tarefas)
    

def main():
    lista_tarefa = []
    lista_lixeira = []

    opcoes = input('Comandos: Listar, Desfazer e Refazer\nDigite sua tarefa ou um comando:').lower()

    
    if opcoes == 'listar':
        listar(lista_tarefas)
    elif opcoes == 'desfazer':
        pass
    elif opcoes == 'refazer':
        pass
    else:
        pass
    

main()