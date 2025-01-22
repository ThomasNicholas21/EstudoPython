# Banco de Dados com Python
Anotações destinadas a manipulação de Banco de Dados utilizando Python.

## sqlite3
Utilizando sqlite3 como banco de dados

### Comandos:
_Iniciar Conexão_ / _Fazer Commits_ / _Fechar Conexão_
```Python
connection = sqlite3.connect(__dbpath__)

# código
connection.commit()


# código
connection.commit()

connection.close()
```
_Executar Ações_
```Python
# Deve estar criado a instância de conexão
cursor = connection.cursor()

cursor.execute(querys)

cursor.close()
```

### Querys:
_Table_
```Python
connection = sqlite3.connect(__dbpath__)
cursor = connection.cursor()

# Criando Querys Table
querys = (
    F'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)

cursor.execute(querys)
connection.commit()

cursor.close()
connection.close()
```
