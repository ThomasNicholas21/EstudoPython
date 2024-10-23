import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NOME = 'db_estudo.sqlite3'
DB_FILE = ROOT_DIR / DB_NOME # Realiza a concatenação entre o caminho do arquivo e o nome da database
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)  
cursor = connection.cursor() 

cursor.execute(f'SELECT * FROM {TABLE_NAME}')

for row in cursor.fetchall(): # função fetchall retorna uma lista de uma consulta realizada
    _id, _name, _weight = row
    print(_id, _name, _weight)


print()

cursor.close()
cursor = connection.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE id = "3"')

row = cursor.fetchone()
_id, _name, _weight = row
print(_id, _name, _weight)

print()

cursor.close()
cursor = connection.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE weight BETWEEN "90" and "110"')

row = cursor.fetchall()
for info in row:
    _id, _name, _weight = info
    print(_id, _name, _weight)

cursor.close()
connection.close()