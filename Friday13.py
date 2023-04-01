import datetime

def friday_the_13th():
    x = datetime.datetime.now()

    print(x + timedelta(day=10))


friday_the_13th()