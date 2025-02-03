# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mensagem de ajuda',
    # type=str,
    metavar='STRING',
    default='Hello World',  # Valor padrão
    required=False,
    # nargs='+',  # cria uma lista dos argumentos
    action='append'  # Recebe mais de uma vez
    )

args = parser.parse_args()

if args.basic is None:
    print('Não passou valor de b')
else:
    print('b:', args.basic)
