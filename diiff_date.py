from datetime import date
y=int(input("enter the year"))
m=int(input("enter the month"))
d=int(input("enter the day"))
y1=int(input("enter the year"))
m1=int(input("enter the month"))
d1=int(input("enter the day")
from_date = date(y, m, d)

to_date = date(y1, m1, d1)
x = to_date - from_date
print(x.days, "days")
