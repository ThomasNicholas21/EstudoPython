import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NOME = 'db_estudo.sqlite3'
DB_FILE = ROOT_DIR / DB_NOME # Realiza a concatenação entre o caminho do arquivo e o nome da database
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)  # Iniciar a conecção
cursor = connection.cursor() # Cursor executa consulta, seleciona, elimina e etc

# SQL

# cursor.execute(
#     f'DELETE FROM {TABLE_NAME}'
# )

# connection.commit()

# SQL INJECTION: Jeito malicioso de burlar comando SQL ao receber informações do usuário
# ao invés de receber um UserName, recebe um comando SQL deixando dados de outros usuários
# vulneráveis. Para evitar e tornar mais seguro, seria utilizar bindings, placeholders etc
# Será responsável por executar querys
sql_create_table = (F'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
) # criando um variável que estará recebendo o comando sql

# cursor.execute(

# )
# connection.commit() # Faz o commit das informaçoes
sql_insert_user = (f'INSERT INTO {TABLE_NAME} (name, weight)'
                    'VALUES (?, ?)') # A interrogação se chamada binding 
# Passa a tratar os valores recebidos como dados e não como comandos

cursor.executemany(sql_insert_user, [['Fulano', 112], ['Ciclano', 90], ['Beltrano', 95]] ) # Tratando como dados
# executemany realiza a execução de diversos comandos
connection.commit()
# Sempre é necessário fechar aquilo que se for aberto para evitar erros
cursor.close()
connection.close()