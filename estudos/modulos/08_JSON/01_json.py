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