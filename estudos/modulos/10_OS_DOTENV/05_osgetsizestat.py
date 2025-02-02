#  os.path.getsize e os.stat (retorna permissao do arquivo)
#  para dados dos arquivos
from itertools import count
import math
import os


def formata_tamanho(tamanho_em_bytes: int, base: int = 1024) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado"""
    # Original:
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python
    # Se o tamanho for menor ou igual a 0, 0B.
    if tamanho_em_bytes <= 0:
        return "0B"
    # Tupla com os tamanhos
    #                      0    1     2     3     4     5
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    # Logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # math.log vai retornar o logaritmo do tamanho_em_bytes
    # com a base (1000 por padrão), isso deve bater
    # com o nosso índice na abreviação dos tamanhos
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    # Por quanto nosso tamanho deve ser dividido para
    # gerar o tamanho correto.
    potencia = base ** indice_abreviacao_tamanhos
    # Nosso tamanho final
    tamanho_final = tamanho_em_bytes / potencia
    # A abreviação que queremos
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'


caminho = os.path.join('C:', '/Teste', 'estudo', 'estudos', 'modulos')
contador = count()

for root, dirs, files in os.walk(caminho):
    o_contador = next(contador)
    print(o_contador, root)

    for _dirs in dirs:
        print(o_contador, _dirs)

    for file in files:
        caminho_arquivo = os.path.join(root, file)
        tamanho = os.path.getsize(caminho_arquivo)
        stats = os.stat(caminho_arquivo)
        status = stats.st_size
        print(
            o_contador, caminho_arquivo, formata_tamanho(tamanho),
            formata_tamanho(status)
            )
