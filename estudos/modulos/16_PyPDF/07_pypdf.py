# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
from pathlib import Path
from PyPDF2 import PdfReader

PATH_ROOT = Path(__file__).parent
PATH_PDF = PATH_ROOT / 'path_pdf'
PATH_PASTE = PATH_ROOT / 'arquivo_novos'

PATH_RELATORIO = PATH_PDF / 'expectativamercado.pdf'
PATH_PASTE.mkdir(exist_ok=True)

reader = PdfReader(PATH_RELATORIO)

# iterável que permite ler a quantidade de páginas do PDF
print(len(reader.pages))

for page in reader.pages:
    print(page)
