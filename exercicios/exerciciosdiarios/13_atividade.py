# Dia 13: Arquivos (Escrita)
# Faça um programa que pergunte ao usuário por uma lista de tarefas e as salve em um arquivo de texto.
from pathlib import Path

ROOT_DIR = Path(__file__).parent
TXT_NAME = '13_atividade.txt'
TXT_FILE = ROOT_DIR / TXT_NAME

class Tarefas:
    def __init__(self, tarefa) -> None:
        self.tarefa = tarefa

    def criar_tarefa(self, lista: list):
        lista.append(self.tarefa)

    def deletar_tarefa(self, lista: list):
        lista.remove(self.tarefa)

    def __repr__(self) -> str:
        return f'{self.tarefa}'

class GerarTarefaTXT:
    def __init__(self, caminho_arquivo) -> None:
        self.caminho_arquivo = caminho_arquivo
        self.modo = 'w'
        self._abrir_arquivo = None

    def __enter__(self):
        print('Gravando tarefas')
        self._abrir_arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._abrir_arquivo

    def __exit__(self, class_exception_, exception_, traceback_):
        print('Gravação finalizada.')
        self._abrir_arquivo.close()

def criar_tarefas(lista_tarefas):
    atividade = input('Digite sua tarefa: ')
    tarefa = Tarefas(atividade)
    tarefa.criar_tarefa(lista_tarefas)
    print('Tarefa criada.\n')

def deletar_tarefas(lista_tarefas):
    atividade = input('Digite a tarefa: ')
    if atividade in lista_tarefas:
        tarefa = Tarefas(atividade)
        tarefa.deletar_tarefa(lista_tarefas)
        print('Tarefa deletada.\n')
    else:
        print('Não foi encontrado essa tarefa.')

def listar_tarefas(lista_tarefas):
    print('Lista de tarefas:')
    if lista_tarefas:
        for contador, tarefa in enumerate(lista_tarefas):
            print(f'Atividade {contador + 1}: {tarefa}')
        print()

    else:
        print('Sem tarefas aqui...\n')

def gravar_tarefas(lista_tarefas):
    with GerarTarefaTXT(TXT_FILE) as arquivo:
        for contador ,tarefa in enumerate(lista_tarefas):
            arquivo.writelines(f'Atividade {contador + 1}: {tarefa}\n')
        print()


def processar_tarefas(lista_tarefas):
    comandos = input('Comandos Tarefa: Criar, Deletar, Listar, Gravar e Sair\n-->').lower().strip()

    match comandos:
        case 'criar':
            criar_tarefas(lista_tarefas)
            return True
        case 'deletar':
            deletar_tarefas(lista_tarefas)
            return True
        case 'listar':
            listar_tarefas(lista_tarefas)
            return True
        case 'gravar':  
            gravar_tarefas(lista_tarefas) 
            return True
        case 'sair':
            return False
        case _:
            print('Opção inválida, digite um comando que exista.')
            return True
        
def main():
    lista_tarefas = []

    while True:
        processos = processar_tarefas(lista_tarefas)
        if not processos:
            break

if __name__ == "__main__":
    main()