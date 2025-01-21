# estudo sobre módulo requests
import requests

# http -> porta 80
# https -> porta 443
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

# exemplos de uso
#print(response.status_code, response.url, response.content, response.text, response.json, sep='\n\n')

# como acessar dados de uma API
data = response.json()
print(data[0]['title'])
print(data[1]['title'])
print(data[2]['title'])
