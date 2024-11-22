# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# Timestamp Unix contagem de segundos 01/01/1970
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta # um timedelta "completo"
# classdateutil.relativedelta.relativedelta(dt1=None, dt2=None, years=0, months=0, 
# #days=0, leapdays=0, weeks=0, hours=0, minutes=0, seconds=0, microseconds=0, year=None, 
# #month=None, day=None, weekday=None, yearday=None, nlyearday=None, hour=None, minute=None, 
# second=None, microsecond=None)

if __name__ == '__main__':
    data1 = datetime.now()
    print(data1.timestamp()) #  numero de segundos de 1970 até a data atual
    print(datetime.fromtimestamp(0)) # 1969-12-31 21:00:00

    formato = '%d/%m/%Y %H:%M:%S'
    data2 = datetime.strptime('21/11/2024 21:06:30', formato)
    data3 = datetime.strptime('31/12/1969 21:00:00', formato)
    data_dif = data2 - data3
    print(f'Diferença {data2} e {data3}', data_dif, 
          data_dif.days, data_dif.seconds, 
          data_dif.total_seconds(), sep=' | ')
    
    data_soma1 = timedelta(days=10, seconds=5) # timedelta representa duração
    print(data3 + data_soma1)

    data_soma2 = relativedelta(years=1000)
    print(data2 + data_soma2)

    delta = relativedelta(data2, data3)
    print(f'Diferença\nDias:{delta.days}\nMês:{delta.months}\nAnos:{delta.years}')