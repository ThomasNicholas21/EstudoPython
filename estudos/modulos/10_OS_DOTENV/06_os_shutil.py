# os + shutil -> mover, copiar e apagar arquivos
# Copiar de uma pasta para outra
# Copiar -> shutil.copy
# Utilizando pastas locais
import os
import shutil

# Chamando o caminho da home do usuário
HOME = os.path.expanduser('~')
print(HOME)

DOCUMENTS = os.path.join(HOME, 'Documents')
DOCUMENTS_ = os.path.join(HOME, 'Documents', 'estudo_teste')
NOVA_PASTA = os.path.join(DOCUMENTS, 'nova_pasta')

# cria nova pasta no diretório e o parâmetro
# exist_ok evita criar outra pasta
os.makedirs(NOVA_PASTA, exist_ok=True)

for root, dirs, files in os.walk(DOCUMENTS_):
    for file in files:
        caminho_origin = os.path.join(root, file)
        caminho_novo_arquivo = os.path.join(
            root.replace(DOCUMENTS_, NOVA_PASTA), file
            )
        shutil.copy(caminho_origin, caminho_novo_arquivo)
        print(file, os.path.getsize(caminho_origin))


print(DOCUMENTS)
