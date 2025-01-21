# Principais Métodos/Funções do Módulo `requests` para Trabalhar com APIs e Requisições HTTP

## 1. Métodos HTTP
Estes são os métodos principais para enviar requisições HTTP.

### **GET**
Usado para buscar dados de um servidor.
```python
response = requests.get("https://api.exemplo.com/dados")
```

### **POST**
Envia dados ao servidor, geralmente para criar um novo recurso.
```python
response = requests.post("https://api.exemplo.com/dados", json={"chave": "valor"})
```

### **PUT**
Atualiza um recurso existente no servidor.
```python
response = requests.put("https://api.exemplo.com/dados/1", json={"chave": "novo_valor"})
```

### **DELETE**
Remove um recurso do servidor.
```python
response = requests.delete("https://api.exemplo.com/dados/1")
```

### **HEAD**
Busca apenas os cabeçalhos da resposta, sem o corpo.
```python
response = requests.head("https://api.exemplo.com/dados")
```

### **OPTIONS**
Obtém informações sobre os métodos suportados pelo servidor para a URL.
```python
response = requests.options("https://api.exemplo.com/dados")
```

### **PATCH**
Usado para realizar atualizações parciais em um recurso.
```python
response = requests.patch("https://api.exemplo.com/dados/1", json={"chave": "valor_parcial"})
```

---

## 2. Parâmetros Úteis

### **`params`**
Envia parâmetros na URL (query string) para requisições GET.
```python
response = requests.get("https://api.exemplo.com/dados", params={"userId": 1, "id": 1})
```

### **`json`**
Envia dados no formato JSON em requisições como POST, PUT ou PATCH.
```python
response = requests.post("https://api.exemplo.com/dados", json={"chave": "valor"})
```

### **`data`**
Envia dados no formato de formulário.
```python
response = requests.post("https://api.exemplo.com/dados", data={"campo1": "valor1"})
```

### **`headers`**
Adiciona cabeçalhos HTTP personalizados à requisição.
```python
headers = {"Authorization": "Bearer <token>"}
response = requests.get("https://api.exemplo.com/dados", headers=headers)
```

### **`timeout`**
Define um tempo limite para a requisição (em segundos).
```python
response = requests.get("https://api.exemplo.com/dados", timeout=5)
```

---

## 3. Acessando Dados da Resposta

### **`response.status_code`**
Obtém o código de status da resposta.
```python
print(response.status_code)  # Exemplo: 200
```

### **`response.json()`**
Converte o conteúdo da resposta em um objeto Python (geralmente dicionário ou lista).
```python
data = response.json()
```

### **`response.text`**
Obtém o conteúdo bruto da resposta como uma string.
```python
print(response.text)
```

### **`response.content`**
Obtém o conteúdo bruto da resposta como bytes.
```python
print(response.content)
```

### **`response.headers`**
Acessa os cabeçalhos da resposta.
```python
print(response.headers)
```

---

## 4. Exceções Comuns

### **`requests.exceptions.RequestException`**
Classe base para todas as exceções no módulo `requests`. Pode ser usada para capturar qualquer erro.
```python
try:
    response = requests.get("https://api.exemplo.com/dados", timeout=5)
    response.raise_for_status()  # Gera exceção para status 4xx/5xx
except requests.exceptions.RequestException as e:
    print("Erro na requisição:", e)
```

### **Exceções Específicas:**
- `requests.exceptions.Timeout`: Acontece quando o tempo limite da requisição é atingido.
- `requests.exceptions.ConnectionError`: Falha na conexão com o servidor.
- `requests.exceptions.HTTPError`: Para códigos de erro HTTP como 404 ou 500.
- `requests.exceptions.URLRequired`: URL inválida ou ausente.

---

## 5. Sessões (session)

Se você precisar fazer múltiplas requisições para o mesmo servidor, pode usar `requests.Session` para compartilhar configurações (como cabeçalhos ou cookies):

```python
with requests.Session() as session:
    session.headers.update({"Authorization": "Bearer <token>"})
    response = session.get("https://api.exemplo.com/dados")
    print(response.json())
```

---

## 6. Upload e Download de Arquivos

### **Enviar arquivos**
```python
files = {"arquivo": open("meuarquivo.txt", "rb")}
response = requests.post("https://api.exemplo.com/upload", files=files)
```

### **Baixar arquivos**
```python
response = requests.get("https://api.exemplo.com/download")
with open("arquivo_baixado.txt", "wb") as file:
    file.write(response.content)
```
