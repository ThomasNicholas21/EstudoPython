# Sào estruturas utilizadas para repetir um trecho de código
# um determinado número de vezes.

# Comando 'for':
# utilizado para percorrer um objeto iterável, sendo utilizado
# quando sabemos a quantidade de vezes que o código deve ser utilizado.
# Exemplo

# nome = 'Thomas'
# vogais = 'aeiou'

# for letra in nome:
#     if letra.lower() in vogais:
#         print(letra)
# else:
#     print('Finalizado')

# # Exemplo

# for contador in range(0, 10, 1):
#     print(contador)

# for contador in range(0, 10, 2):
#     print(contador)

# Comando While
# Repete o bloco de um código várias vezes, fazendo
# sentido utilzar quando não se sabe o número exato
# de vezes que o código deve ser utilizado.
# Exemplo

cadastro = []
opcao = -1
while opcao != 0:
    opcao = int(input('Deseja:\n[1]Cadastrar\n[2]Listar Credenciais\n[0]Sair\nSelecione:'))
    if opcao == 1:
        nome = input('Digite seu nome:')
        sobrenome = input('Digite seu sobrenome: ')
        print('Cadastrado!\n')
        cadastro.append({'Nome': nome, 'Sobrenome': sobrenome})
    elif opcao == 2:
        for chave in cadastro:
            print(chave, sep='\n')
        print()
    else:
        print('Opção invalida.')
else:
    print('Obrigado!')

# Comando break:
# O comando break é usado para interromper a execução de um loop antes que ele termine naturalmente.
# Comando continue
# Pula a iteracao do loop e passa para proxima iteracao (ignora uma iteracao)
# Comando pass
# Operacao nula, nada acontece quando executado, sendo utilizado como placeholder