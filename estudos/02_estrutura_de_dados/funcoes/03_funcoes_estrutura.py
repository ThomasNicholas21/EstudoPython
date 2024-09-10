# Estruturacao de parametros
# Parametros sao passados por posicao, posicao e nome, ou por nome
# def(      p1, p2,       /, p3 or c,         *,    c1, c2   )
#      apenas posicao       posicao              apenas chave
#                            chave
# O que define isso é a barra e o asterisco
#exemplo
def inserir_celular(marca, modelo, /, tamanho, ano):
    return f'Celular: {marca}, {modelo}, {tamanho}, {ano}'

print(inserir_celular("Samsung", "S21", "6,2", "2021")) # não retorna erro pois a direita da barra é opcional
print(inserir_celular("Samsung", "S21", tamanho="6,2", ano="2021")) 
#print(inserir_celular(marca="Samsung", modelo="S21", tamanho="6,2", ano="2021")) # retorna erro pois marca e modelo deve ser posicional
#print(inserir_celular(**{"marca": "Samsung", "modelo": "S21","tamanho": "6,2","ano": "2021"})) # retorna erro pois deve ter argumentos posicionais
print()

def inserir_celular(*, marca, modelo, tamanho, ano):
    return f'Celular: {marca}, {modelo}, {tamanho}, {ano}'

# print(inserir_celular("Samsung", "S21", "6,2", "2021")) # retorna erro pois a funcao aceita apenas argumentos chave e valor
# print(inserir_celular(marca="Samsung", modelo="S21", tamanho="6,2", ano="2021")) # retorna erro pois a funcao aceita apenas argumentos chave e valor
print(inserir_celular(**{"marca": "Samsung", "modelo": "S21","tamanho": "6,2","ano": "2021"}))
print()

def inserir_celular(marca, modelo, /, *, tamanho, ano):
    return f'Celular: {marca}, {modelo}, {tamanho}, {ano}'

print(inserir_celular("Samsung", "S21", tamanho="6,2", ano="2021")) # aceita somente metade posicional e chave e valor