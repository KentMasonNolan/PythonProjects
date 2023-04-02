from datetime import datetime, timedelta

day = 13
month = 4
year = 2023

y = datetime.now()

y = datetime(year, month, day)

friday = False
while friday == False:
    y = datetime(year, month, day)
    if month == 12:
        month = 1
    else:
        month += 1
    if y.strftime("%A") == "Friday":
        print("Friday the 13th will happen on: ")
        print(y.strftime("%Y-%m-%d"))
        friday = True