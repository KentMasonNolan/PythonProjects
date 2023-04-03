from datetime import datetime, timedelta

def friday_the_13th():

    y = datetime.now()
    # y = datetime(2025, 6, 12)

    isFriday = False
    day = y.day
    month = y.month
    year = y.year

    if day < 13:
        day = 13
    else:
        day = 13
        month += 1

    y = datetime(year, month, day)

    while isFriday == False:
        day = 13
        y = datetime(y.year, y.month, day)
        if y.strftime("%A") == "Friday":
            print(y.strftime("%Y-%m-%d"))
            isFriday = True
            return y.strftime("%Y-%m-%d")
        else:
            y = y + timedelta(days=22)

friday_the_13th()