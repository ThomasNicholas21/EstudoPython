# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime

if __name__ == "__main__":
    # datetime(ano, mês, dia, horas, minutos, segundos, microssegundos (10*6 segundos), timezone)
    # opcional após dia
    data1 = datetime(2000, 12, 31)
    data2 = datetime(2000, 12, 31, 23, 59, 59, 999999)
    print(data1, data2, sep='\n')
    #utilizando diretivas do datetime
    data3 = '2000-12-20 01:12:54'
    data_formato1 = '%Y-%m-%d %H:%M:%S'
    data_formato2 = '%a-%B-%y %I:%M:%S %p'
    print(datetime.strptime(data3, data_formato1))
    print(datetime.now().strftime(data_formato2))

