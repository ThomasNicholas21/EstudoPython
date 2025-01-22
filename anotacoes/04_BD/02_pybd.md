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

