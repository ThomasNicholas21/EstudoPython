# Lista de Tarefas
# Definição: realizar a listagem, desfaz uma ação e refazaz uma ação 
import os

class lista_tarefas:
    def __init__(self, lista):
        self.lista = lista
    
    def inserir_tarefa(self, valor):
        self.lista.append(valor)

    def apaga_tarefa(self, lista_lixeira):
        if self.lista:
            valor = self.lista.pop()
            lista_lixeira.append(valor)

    def refaz_tarefa(self, lista_lixeira):
        if lista_lixeira:
            valor = lista_lixeira.pop()
            self.lista.append(valor)

    def __str__(self):
        return f'{self.__class__.__name__}:\n{'\n'.join([f'{item}' for item in self.lista])}'

def listar(lista_tarefa):
    tarefas = lista_tarefas(lista_tarefa)
    print(tarefas)

def inserir_tarefa(lista_tarefa, tarefas):
    tarefa = lista_tarefas(lista_tarefa)
    tarefa.inserir_tarefa(tarefas)
    
def desfazer(lista_tarefa, lista_lixeira):
    tarefa = lista_tarefas(lista_tarefa)
    tarefa.apaga_tarefa(lista_lixeira)

def refazer(lista_tarefa, lista_lixeira):
    tarefa = lista_tarefas(lista_tarefa)
    tarefa.refaz_tarefa(lista_lixeira)

def main():
    lista_tarefa = []
    lista_lixeira = []

    while True:
        opcoes = input('Comandos: Listar, Desfazer e Refazer\nDigite sua tarefa ou um comando:').lower()

        if opcoes == 'listar':
            if not lista_tarefa:
                print('Lista vazia.')
            else:
                listar(lista_tarefa)
                print()
        elif opcoes == 'desfazer':
            if not lista_tarefa:
                print('Nada a desfazer.\n')
            else:
                desfazer(lista_lixeira, lista_lixeira)
                print()
        elif opcoes == 'refazer':
            if not lista_tarefa and not lista_lixeira:
                print('Nada a refazer.\n')
            else:
                refazer(lista_tarefa, lista_lixeira)
                print()
        elif opcoes == 'sair':
            break
        elif opcoes == 'limpar':
            os.system('cls')
        else:
            inserir_tarefa(lista_tarefa, opcoes)
    
main()