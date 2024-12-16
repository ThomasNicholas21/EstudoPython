# json.dumps e json.loads com strings + typing.TypedDict
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null

import json
from typing import TypedDict # biblioteca permite que realize a tipagem de um dicionario
from pathlib import Path

ROOT_DIR = Path(__file__).parent
JSON_NAME = 'filme.json'
FILE = ROOT_DIR / JSON_NAME

class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: True | False
    imdb_rating: float
    year: int
    characters: list | tuple
    budget: float

filme = '''
{
  "title": "Interestelar",
  "original_title": "Interstellar",
  "is_movie": true,
  "imdb_rating": 8.7,
  "year": 2014,
  "characters": ["Tars", "Amelia", "Murphy", "Cooper", "Romilly"],
  "budget": 165000000
}
'''

def printd(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

if __name__ == "__main__":
    filme_json: Movie = json.loads(filme)
    printd(**filme_json)

    filme_json_string = json.dumps(filme_json, ensure_ascii=False, indent=2)
    with open(FILE , 'w') as arquivo:
        json.dump(filme_json_string, arquivo)
