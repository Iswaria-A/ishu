import datetime
now=datetime.datetime.now()
print("Current date and time:")
print(now.strftime("%y-%m-%d %H:%M:%S"))

today=datetime.datetime.today()
print("Current year:")
print(today.strftime("%Y"))

today=datetime.datetime.today()
print("Month of the year:")
print(today.strftime("%B"))

today=datetime.datetime.today()
print("Week number of the year:")
print(today.strftime("%W"))

today=datetime.datetime.today()
print("Week day of the week:")
print(today.strftime("%w"))

today=datetime.datetime.today()
print("Day of the year:")
print(today.strftime("%j"))

today=datetime.datetime.today()
print("Day of the month:")
print(today.strftime("%d"))

today=datetime.datetime.today()
print("Day of the week:")
print(today.strftime("%A"))