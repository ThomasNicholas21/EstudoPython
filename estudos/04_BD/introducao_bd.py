import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NOME = 'db_estudo.sqlite3'
DB_FILE = ROOT_DIR / DB_NOME # Realiza a concatenação entre o caminho do arquivo e o nome da database

connection = sqlite3.connect(DB_FILE)  # Iniciar a conecção
cursor = connection.cursor() # Cursor executa consulta, seleciona, elimina e etc

# SQL

# Sempre é necessário fechar aquilo que se for aberto para evitar erros
cursor.close()
connection.close()