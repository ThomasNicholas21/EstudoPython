from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    idade: int

    @property
    def nome_completo(self) -> str:
        return f'{self.nome}{self.sobrenome}'
    
    @nome_completo.setter
    def nome_completo(self, valor: str) -> str:
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.nome = sobrenome

