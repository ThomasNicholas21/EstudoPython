# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime, timedelta, timezone
from pytz import timezone as tz # simplifica a chamada das timezones

if __name__ == "__main__":
    data1 = datetime.now(tz('Asia/Tokyo')) 
    data2 = datetime.now(tz('Australia/Sydney'))
    data3 = datetime.now(tz('America/Denver'))
    print(f'Tokyo: {data1}\nAustralia: {data2}\nDenver{data3}')

    fuso_horario = timezone(timedelta(hours=12))
    data4 = datetime.now(fuso_horario)
    print(f'Antarctica: {data4}')
    