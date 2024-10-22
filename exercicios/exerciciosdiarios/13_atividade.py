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
        self.abrir_arquivo = None

    def __enter__(self):
        pass

    def __exit__(self):
        pass

def main():
    pass

if __name__ == "__main__":
    main()