from datetime import datetime, timedelta

day = 13
month = 4
year = 2023

x = datetime.now()
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
        print(str(y))
        friday = True
    # print(y.strftime("%A"))

# print(x.year)
# print(x.strftime("%A"))
#
# print("Y: ")
# print(y.strftime("%A"))
# print(y.strftime("%D"))
#
# x = x + timedelta(days=2)
#
# print(x.year)
# print(x.strftime("%A"))
#
# if x.strftime("%A") == "Monday":
#     print("Hello")
# else: print("Not Monday")