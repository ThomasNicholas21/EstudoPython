# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.




# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo
import calendar as cd


# Com calendar, você pode saber coisas como:
print(cd.calendar(2024))
print(cd.month(2024, 11))
# - Qual o último dia do mês (ex.: monthrange)
print(cd.monthrange(2024, 2)) # (3, 29) representa qual dia da semana e o ultimo dia do mês
print(list(cd.day_name))
# - Qual o nome e número do dia de determinada data (ex.: weekday)
print(cd.weekday(2024, 12, 5)) # retorna qual dia mês que no caso seria quinta (thursday)
# - Criar um calendário em si (ex.: monthcalendar)

month_calendar = [list(enumerate(semana)) for semana in cd.monthcalendar(2024, 10)]
print(*month_calendar, sep='\n') # '0' representa os dias que não são da semana