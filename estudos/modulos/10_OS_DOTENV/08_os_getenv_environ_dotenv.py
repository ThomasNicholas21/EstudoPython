# Variáveis de ambiente com Python
# Para variáveis de ambiente
# Windows PS: $env:VARIAVEL="VALOR" | dir env:
# Linux e Mac: export NOME_VARIAVEL="VALOR" | echo $VARIAVEL
# Para obter o valor das variáveis de ambiente
# os.getenv ou os.environ['VARIAVEL']
# Para configurar variáveis de ambiente
# os.environ['VARIAVEL'] = 'valor'
# Ou usando python-dotenv e o arquivo .env
# pip install python-dotenv
# from dotenv import load_dotenv
# load_dotenv()
# https://pypi.org/project/python-dotenv/
# OBS.: sempre lembre-se de criar um .env-example
import os
from dotenv import load_dotenv


# .env é um ambiente que não vai para nenhum
# repositório, no qual tem configurações do
# ambiente. O load_dotenv() carrega as variáveis
# criadas
load_dotenv()

# Pega todas as variáveis do sistemas operacional
# incluindo a do .env
# print(os.environ)

# Pega uma variável especificada
print(os.getenv('BD_USER'))
