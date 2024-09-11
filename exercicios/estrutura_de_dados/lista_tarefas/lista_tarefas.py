# Lista de Tarefas
# Definição: realizar a listagem, desfaz uma ação e refazaz uma ação 
import os
import json

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
    if not lista_tarefa:
        return print('Lista vazia.')
    
    tarefa = lista_tarefas(lista_tarefa)
    print(tarefa)
    print()

def inserir_tarefa(lista_tarefa, tarefas):
    tarefa = lista_tarefas(lista_tarefa)
    tarefa.inserir_tarefa(tarefas)
    
def desfazer(lista_tarefa, lista_lixeira):
    if not lista_tarefa:
        return print('Nada a desfazer.\n')
    
    tarefa = lista_tarefas(lista_tarefa)
    tarefa.apaga_tarefa(lista_lixeira)
    print()

def refazer(lista_tarefa, lista_lixeira):
    if not lista_lixeira:
        print('Nada a refazer.\n')

    tarefa = lista_tarefas(lista_tarefa)
    tarefa.refaz_tarefa(lista_lixeira)
    print()

def exportar(lista_tarefa):
    with open("D:/programação/EstudoPython/exercicios/estrutura_de_dados/lista_tarefas/lista_tarefas.json", "w") as arquivo:
        json.dump(lista_tarefa, arquivo, indent=2)

def main():
    lista_tarefa = []
    lista_lixeira = []

    while True:
        opcoes = input('Comandos: Listar, Desfazer, Refazer e Exportar\nDigite sua tarefa ou um comando:').lower()

        if opcoes == 'listar':
            listar(lista_tarefa)
        elif opcoes == 'desfazer':
            desfazer(lista_tarefa, lista_lixeira)
        elif opcoes == 'refazer':
            refazer(lista_tarefa, lista_lixeira)
        elif opcoes == 'exportar':
            exportar(lista_tarefa)
        elif opcoes == 'sair':
            break
        elif opcoes == 'cls':
            os.system('cls')
        else:
            inserir_tarefa(lista_tarefa, opcoes)
            print()

main()