# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# Timestamp Unix contagem de segundos 01/01/1970
from datetime import datetime

if __name__ == '__main__':
    data1 = datetime.now()
    print(data1.timestamp()) #  numero de segundos de 1970 até a data atual
    print(datetime.fromtimestamp(0)) # 1969-12-31 21:00:00