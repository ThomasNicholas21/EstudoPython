import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NOME = 'db_estudo.sqlite3'
DB_FILE = ROOT_DIR / DB_NOME # Realiza a concatenação entre o caminho do arquivo e o nome da database
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)  # Iniciar a conecção
cursor = connection.cursor() # Cursor executa consulta, seleciona, elimina e etc

# SQL

cursor.execute(
    f'DELETE FROM {TABLE_NAME}' # DELETE sem WHERE apaga todos os dados da tabela
)

cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name={TABLE_NAME}' # apaga o autoincremente definido no ID dos usuários
)

# Realizar commit para as alterações serem feitas

# SQL INJECTION: Jeito malicioso de burlar comando SQL ao receber informações do usuário
# ao invés de receber um UserName, recebe um comando SQL deixando dados de outros usuários
# vulneráveis
# Será responsável por executar querys
cursor.execute(
    F'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit() # Faz o commit das informaçoes

cursor.execute( # Executa um comando, enquanto executemany executa várias
    f'INSERT INTO {TABLE_NAME} (id, name, weight)'
    'VALUES (NULL, "Thomas", 75)'
)

connection.commit()
# Sempre é necessário fechar aquilo que se for aberto para evitar erros
cursor.close()
connection.close()