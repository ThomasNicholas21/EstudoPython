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
sql_selectall = (
     f'SELECT * FROM {TABLE_NAME}'
)

sql_selectone = (
     f'SELECT * FROM {TABLE_NAME} WHERE weight = "82"'
)

cursor.execute(sql_selectall)

for row in cursor.fetchall():
    _id, _name, _weight = row
    print(_id, _name, _weight)
print()

cursor.execute(sql_selectone)

row = cursor.fetchone()
print(*row)


# CR [UPDTADE] D

# CRU [DELETE]

sql_delete_sem_where = (f'DELETE FROM {TABLE_NAME}') # Delete sem where (perigoso), pode deletar todos os dados 

sql_dele_com_where = (f'DELETE FROM {TABLE_NAME} WHERE name = "Beltrano"')

sql_delete_sequencia = (f'DELTE FROM sqlite_sequence WHERE name="{TABLE_NAME}"')

# cursor.execute(sql_dele_com_where)
# connection.commit()

cursor.close()
connection.close()