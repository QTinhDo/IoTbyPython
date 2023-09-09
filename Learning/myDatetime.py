
from datetime import date

# print("Today:", date.today())
# print("Day:", date.today().day)
# print("Month:", date.today().month)
# print("Month:", date.today().year)

# print("WeekDay:", date.today().weekday()+2)


from datetime import datetime

# print("Today:", datetime.now())
# print("Hour:", datetime.now().hour)
# print("Minute:", datetime.now().minute)

# now = datetime.now()

# print(now.strftime("Year: %Y"))
# print(now.strftime("Month: %m"))
# print(now.strftime("Day: %d"))

from datetime import timedelta

print("Thong tin cua 1 gio sau: ")
print(datetime.now() + timedelta(hours=1, minutes=00))
