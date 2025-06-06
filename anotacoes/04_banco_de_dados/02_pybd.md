# Banco de Dados com Python
Anotações destinadas a manipulação de Banco de Dados utilizando Python.

## sqlite3
Utilizando sqlite3 como banco de dados

## SQL injection
Jeito malicioso de burlar comando SQL ao receber informações do usuário ao invés de receber um UserName, recebe um comando SQL deixando dados de outros usuários vulneráveis. Para evitar e tornar mais seguro, seria utilizar bindings, placeholders e etc.
```Python
# utilizando listas
insert = (
    f'INSERT INTO {TABLE_NAME} (name, weight)'
     'VALUES (?, ?)' # bindings
)

cursor.executemany(insert, [['fulano', 100], ['beltrano', 80]])
```
```Python
# utilizando dics
insert = (
    f'INSERT INTO {TABLE_NAME} (name, weight)'
     'VALUES (name:, weight:)' # bindings
)

cursor.executemany(
    insert, 
    [
        {'name': 'fulano', 'weight': 100},
        {'name': 'beltrano', 'weight': 80}
    ]
)
```
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
_Insert_
```Python
connection = sqlite3.connect(__dbpath__)
cursor = connection.cursor()

# Criando Querys delete
querys_delete1 = (
    F'DELETE FROM {TABLE_NAME}' # apaga todos os dados
)

querys_delete2 = (
    f'DELETE FROM {TABLE_NAME} WHERE name = "Beltrano"' # apaga autoincrement
)

querys_delete3 = (
    f'DELETE FROM sqlite_sequence WHERE name={TABLE_NAME}' # apaga autoincrement
)

cursor.execute(querys, VALUES)
connection.commit()

cursor.close()
connection.close()
```
_Delete_
```Python
connection = sqlite3.connect(__dbpath__)
cursor = connection.cursor()

# Criando Querys Insert
querys = (
    F'INSERT INTO {TABLE_NAME} (name, weight)'
    'VALUES (name, weight)' # pode-se utilizar placeholders/bindings
)

cursor.execute(querys, VALUES)
connection.commit()

cursor.close()
connection.close()
```
_select_
```python
connection = sqlite3.connect(__dbpath__)
cursor = connection.cursor()

# Criando Querys Insert
querys = (
    F'SELECT * FROM {TABLE_NAME} WHERE id = "3"' 
)

cursor.execute(querys, VALUES)

row = cursor.fetchaone()
row = cursor.fetchall()
row = cursor.fetchmany()

cursor.close()
connection.close()
```
_update_
```python
connection = sqlite3.connect(__dbpath__)
cursor = connection.cursor()

# Criando Querys Insert
querys = (
    f'UPDATE {TABLE_NAME} '
    'SET name = "Jorel" '
    'WHERE id = 5 '
)

cursor.execute(querys, VALUES)
connection.commit()

cursor.close()
connection.close()
```