# Diretivas Importantes do Módulo `datetime` em Python

O módulo `datetime` do Python utiliza **diretivas** para formatar e interpretar datas e horários.

## **Diretivas para Datas**
Essas diretivas representam ou interpretam a parte da **data** (ano, mês, dia):

- **`%Y`**: Ano com quatro dígitos.  
  **Exemplo**: `2024`

- **`%y`**: Ano com dois dígitos.  
  **Exemplo**: `24`

- **`%m`**: Mês como número (01 a 12).  
  **Exemplo**: `11`

- **`%B`**: Nome completo do mês.  
  **Exemplo**: `November`

- **`%b`**: Nome abreviado do mês.  
  **Exemplo**: `Nov`

- **`%d`**: Dia do mês como número (01 a 31).  
  **Exemplo**: `14`

- **`%a`**: Nome abreviado do dia da semana.  
  **Exemplo**: `Thu`

- **`%A`**: Nome completo do dia da semana.  
  **Exemplo**: `Thursday`

---

## **Diretivas para Horários**
Essas diretivas manipulam a **hora**, **minutos** e **segundos**:

- **`%H`**: Hora no formato 24h (00 a 23).  
  **Exemplo**: `14`

- **`%I`**: Hora no formato 12h (01 a 12).  
  **Exemplo**: `02`

- **`%p`**: Período (AM/PM).  
  **Exemplo**: `PM`

- **`%M`**: Minutos (00 a 59).  
  **Exemplo**: `45`

- **`%S`**: Segundos (00 a 59).  
  **Exemplo**: `30`

- **`%f`**: Microsegundos (000000 a 999999).  
  **Exemplo**: `123456`

---

## **Diretivas Combinadas**
Essas diretivas incluem informações de tempo e data:

- **`%c`**: Representação completa de data e hora (localizada).  
  **Exemplo**: `Thu Nov 14 14:45:30 2024`

- **`%x`**: Representação apenas da data (localizada).  
  **Exemplo**: `11/14/24`

- **`%X`**: Representação apenas do horário (localizada).  
  **Exemplo**: `14:45:30`

---

## **Outras Diretivas Úteis**
Diretivas específicas para casos comuns:

- **`%j`**: Dia do ano (001 a 366).  
  **Exemplo**: `318`

- **`%U`**: Número da semana do ano (domingo como o primeiro dia da semana).  
  **Exemplo**: `46`

- **`%W`**: Número da semana do ano (segunda-feira como o primeiro dia da semana).  
  **Exemplo**: `45`

- **`%z`**: Fuso horário no formato de deslocamento UTC.  
  **Exemplo**: `+0000`

- **`%Z`**: Nome do fuso horário.  
  **Exemplo**: `UTC`

---

## **Diretivas Mais Comuns no Dia a Dia**
Para tarefas rotineiras, estas são as diretivas mais úteis:

- **Datas**: `%Y`, `%m`, `%d`
- **Horários**: `%H`, `%M`, `%S`
- **Dia e mês**: `%A`, `%a`, `%B`, `%b`
- **Formato 12h**: `%I`, `%p`
- **Combinação completa**: `%c`

---

## **Exemplo de Uso**
```python
from datetime import datetime

# Criar um objeto de data e hora
agora = datetime.now()

# Exemplo de formatação
formato = agora.strftime("%A, %d %B %Y %H:%M:%S")
print(f"Data formatada: {formato}")
# Saída: "Thursday, 14 November 2024 14:45:30"
```

Com estas diretivas, é possível manipular e formatar qualquer data e hora de maneira eficiente.
