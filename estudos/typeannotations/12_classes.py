# é possível utilizar classes para tipar objetos

class Pessoa:
    def __init__(self, primeiro_nome, segundo_nome):
        self.primeiro_nome = primeiro_nome
        self.segundo_nome = segundo_nome

    @property
    def nome_completo(self):
        return f'{self.primeiro_nome} {self.segundo_nome}'


def qual_nome_completo(pessoa: Pessoa) -> str:
    return pessoa.nome_completo


print(qual_nome_completo(Pessoa('Manoel', 'Gomes')))
