import time
from functions import coder

def checker():
    todayDate = time.strftime("%m:%d")
    if todayDate == '2:8':
            return 'Today is your birthday master. I wish you a good day.'

    readen = coder.decoder('data/files/holidays.uiop')
    
    if not(readen):
        return None

    holidayDict = {}

    for i in  readen.split("\n"):
        if not(i.endswith("*")) and i and not( i == ' '):
            data = i.split(" ")
            date = data[0]
            holiday = data[1]
            holidayDict[date] = holiday

    # print(holidayDict)
    greet = None
    for date, holiday in holidayDict.items():
        # print(date)
        if date == todayDate:
            if 'Christmas' in holiday:
                greet = "MARRY " + ' '.join(holiday.split('-'))
            elif 'Birthday' in holiday:
                greet = "Today is " + ' '.join(holiday.split('-'))
            else:
                greet = "HAPPY " + ' '.join(holiday.split('-'))
    
    # print(f"{greet}")
    return greet

def newHoliday():
    pass

# checker()