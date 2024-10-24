import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NOME = 'db_estudo.sqlite3'
DB_FILE = ROOT_DIR / DB_NOME # Realiza a concatenação entre o caminho do arquivo e o nome da database
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)  
cursor = connection.cursor() 

# CRUD
# [CREATE/INSERT] RUD
sql_create = ( 
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)

sql_insert = (
    f'INSERT INTO {TABLE_NAME} (name, weight)'
    'VALUES (:name, :weight)'
)
#cursor.execute(sql_create)
# cursor.executemany(
#     sql_insert, 
#     [{'name': 'Fulano', 'weight': 75}, 
#      {'name': 'Ciclano', 'weight': 82}, 
#      {'name': 'Beltrano', 'weight': 92}]
# )

# C [READ/SELECT] UD

cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)

for row in cursor.fetchall():
    _id, _name, _weight = row
    print(_id, _name, _weight)
print()

cursor.execute(
    f'SELECT * FROM {TABLE_NAME} WHERE weight = "82"'
)

row = cursor.fetchone()
print(*row)

cursor.close()
connection.close()