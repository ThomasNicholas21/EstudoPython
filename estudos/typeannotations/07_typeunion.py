# Type Union

# Tipando para aceitar duas tipagens de variáveis
aceita_duas_tipagens = str | int   # union
digito1: aceita_duas_tipagens = '1' or 1  # Não retorna erro
# digito1: aceita_duas_tipagens = 1   # Não retorna erro
