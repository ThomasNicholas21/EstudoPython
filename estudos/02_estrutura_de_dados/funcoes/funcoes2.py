# Arugmentos nomeados são aqueles nomeados na forma chave=valor

def inserir_celular(marca, modelo, tamanho, ano):
    return f'Celular: {marca}, {modelo}, {tamanho}, {ano}'

print(inserir_celular("Samsung", "S21", "6,2", "2021")) 
print(inserir_celular(marca="Samsung", modelo="S21", tamanho="6,2", ano="2021"))
print(inserir_celular(**{"marca": "Samsung", "modelo": "S21","tamanho": "6,2","ano": "2021"}))
print()

# args e kwargs

def exibe_email(saudacoes, *conteudo, **adeus):
    texto = '\n'.join(conteudo)
    texto_padronizado = '\n'.join([f'{chave.title()}: {valor}' for chave, valor in adeus.items()])
    texto_final = f"{saudacoes}\n\n{texto}\n\n{texto_padronizado}"
    return print(texto_final)


exibe_email(
    "Bom dia", 
    "Pagamento realizado", 
    "Qualquer duvida estamos a disposicao",
    atenciosamente="Thomas",
    data=2024
    )