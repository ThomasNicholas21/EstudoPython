# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html

from datetime import datetime

if __name__ == "__main__":
    formato = '%d/%m/%Y %H:%M:%S'
    data = datetime.strptime('21/12/1988 20:35:45', formato)
    print(data)
    # formta em string
    print(data.strftime('%d/%m/%Y'))
    print(data.strftime('%H:%M:%S'))
    print(data.strftime('%Y'))
    print(data.strftime('%Y %H:%M:%S'))
