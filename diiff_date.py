from datetime import date
y=int(input("enter the year"))
m=int(input("enter the month"))
d=int(input("enter the day"))
from_date = date(y, m, d)
to_date = date(2019, 4, 20)
x = to_date - from_date
print(x.days, "days")
