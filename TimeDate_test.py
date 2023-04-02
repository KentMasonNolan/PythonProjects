from datetime import datetime, timedelta

x = datetime.now()

print(x.year)
print(x.strftime("%A"))

x = x + timedelta(days=2)

print(x.year)
print(x.strftime("%A"))

if x.strftime("%A") == "Monday":
    print("Hello")
else: print("Not Monday")