from datetime import datetime
from pytz import timezone

if __name__ == "__main__":
    data1 = datetime.now(timezone('Asia/Tokyo'))
    data2 = datetime.now(timezone('Australia/Sydney'))
    data3 = datetime.now(timezone('America/Denver'))
    print(data1, data2, data3, sep='\n')