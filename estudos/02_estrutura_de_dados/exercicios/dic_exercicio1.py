# Escreva um programa em Python que leia um texto fornecido pelo usuário e conte 
# a frequência de cada palavra.
# O programa deve ignorar a diferença entre maiúsculas e minúsculas e considerar 
# apenas palavras com caracteres alfabéticos.
import re

def print_dic(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}") 

def contador_texto(texto):
    dic_palavras = {}
    texto_split = re.split(r'[ ,.:;!?]+', texto.lower())
    for palavra in texto_split:
        if palavra:
            dic_palavras.update({palavra: texto_split.count(palavra)})
    return print_dic(**dic_palavras)

texto = input("Insira o seu texto aqui:")
print("Contagem sendo processada...")
contador_texto(texto)