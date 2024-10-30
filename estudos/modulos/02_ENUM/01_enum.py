# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value
# Alguns casos em que o uso de Enum é ideal:
# - Estados ou Fases Finitas: Quando há um conjunto de estados conhecidos, como "Aguardando", "Em Progresso", "Concluído". 
# Isso ajuda a evitar erros e tornar o código mais legível.
# - Categorias ou Tipos: Para representar tipos de um objeto, como "PDF", "TXT", "DOCX" para tipos de arquivos, ou "Admin", "User", "Guest" para tipos de usuários.
# - Validação de Dados: Ao validar valores, Enum restringe as opções possíveis, reduzindo o risco de valores incorretos.
# - Substituir Constantes com Nomes Significativos: Facilita a substituição de constantes numéricas ou 
# strings repetidas que poderiam causar confusão, como códigos de status HTTP (200: OK, 404: Not Found, etc.).
import enum

#Estados = enum.Enum('Estados', ['Iniciando', 'Aguardando', 'Em progresso', 'Concluído']) # Pode ser representado assim, porém a IDE pode não saber tratar o mesmo

class Estado(enum.Enum):
    INICIANDO = enum.auto()
    AGUARDANDO = enum.auto()
    EM_PROGRESSO = enum.auto()
    CONCLUIDO = enum.auto()

def status(estado: Estado):
    if not isinstance(estado, Estado):
        raise ValueError('Estados não definido')
    
    print(f'STATUS: {estado.name}')

print(Estado.INICIANDO, Estado(1), Estado['INICIANDO'], Estado(1).name, Estado.INICIANDO.value, sep=' | ', end='\n')
status(Estado.INICIANDO)
status(Estado.AGUARDANDO)
status(Estado.EM_PROGRESSO)
status(Estado.CONCLUIDO)


