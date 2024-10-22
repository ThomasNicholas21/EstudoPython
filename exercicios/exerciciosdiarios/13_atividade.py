# Dia 13: Arquivos (Escrita)
# Faça um programa que pergunte ao usuário por uma lista de tarefas e as salve em um arquivo de texto.

class Tarefas:
    def __init__(self, tarefa) -> None:
        self.tarefa = tarefa

    def criar_tarefa(self, lista: list):
        lista.append(self.tarefa)

    def deletar_tarefa(self, lista: list):
        lista.remove(self.tarefa)

class GeraTarefaTXT:
    def __init__(self, caminho_arquivo) -> None:
        self.caminho_arquivo = caminho_arquivo
        self.modo = 'w'
        self._abrir_arquivo = None

    def __enter__(self):
        print('Gravando tarefas')
        self._abrir_arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._abrir_arquivo

    def __exit__(self):
        print('Gravação finalizada.')
        self._abrir_arquivo.close()

def criando_tarefas():
    pass

def deletando_tarefas():
    pass

def listar_tarefas():
    pass

def gravar_tarefas():
    pass

def main():
    lista_tarefas = []

if __name__ == "__main__":
    main()