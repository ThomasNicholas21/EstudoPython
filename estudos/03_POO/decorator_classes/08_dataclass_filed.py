from dataclasses import dataclass, field, fields 
#field realiza o controle d que irá ser criado
#fields realiza uma listagem dos metadados da classe

@dataclass
class Pessoa:
    nome: str = 'Fulano'
    sobrenome: str = field(default='Silva')
    enderecos: list[str] = field(default_factory=list) # serve para controle sobre atributos

if __name__ == "__main__":
    print(Pessoa())
    print(fields(Pessoa()))