# Associação
Quado se trata de associação para Programação Orientada a Objetos, se refere a uma classe que terá uma relação direta com outra classe, podendo ter acesso a atributos e métodos dessa classe, sem ter uma dependência rigida e direta da classe.
- *Exemplo*:
    ```Python
    class Professor
        pass

    class Escola
        pass

    # a classe escola pode exoiistir sem um professor específico.
    ```


# Agregação
Uma forma especializada de associação entre dois ou mais objetos. Geralmente é uma relação de um para muitos, onde um objeto tem um ou muitos objetos. Os objetos podem vir separadamente, mas pode se tratar de uma relação onde um objeto precisa de outro para fazer determinada tarefa. Dessa forma, é possível concluir que as classes não depende do objeto como um todo, mas dependem uma das outros para executar algo completo.
- *Exemplo*:
    ```Python
    class Aluno:
    def __init__(self, nome):
        self.nome = nome

    class SalaDeAula:
        def __init__(self):
            self.alunos = []

        def adicionar_aluno(self, aluno):
            self.alunos.append(aluno)

    # Agregação: A SalaDeAula agrega Alunos, mas os alunos existem independentemente
    aluno1 = Aluno("Maria")
    sala = SalaDeAula()
    sala.adicionar_aluno(aluno1)

    ```