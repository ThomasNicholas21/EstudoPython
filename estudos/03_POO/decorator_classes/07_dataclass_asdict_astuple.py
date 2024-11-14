from dataclasses import dataclass, asdict, astuple
# asdict e astuple transforma as dataclasses em dicionarios e tuplas, respectivamente

@dataclass
class Pessoa:
    nome: str
    sobrenome: str

if __name__ == "__main__":
    pessoa1 = Pessoa('Fulano', 'Silva')
    pessoa2 = Pessoa('Ciclano', 'Gomes')
    #print(Pessoa.__dict__)
    print(asdict(pessoa1).values())
    print(asdict(pessoa1).items()) 
    print(asdict(pessoa1).keys())  # Isso transform o objeto em uma dicinario
    print(astuple(pessoa2))