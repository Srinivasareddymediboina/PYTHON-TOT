# import date time Module
from datetime import datetime as dt  
t1=input('enter date in HH:MM:SS:')
t2=input('enter date in HH:MM:SS:')
# format Time
format= "%H:%M:%S"  

def timedifference(time1, time2):
        try:
                t1 = dt .strptime(time2,format)-dt.strptime(time1, format)
                return t1
        except Exception as e:
                print(e)
                return e
        return (t2 - t1)
print(timedifference(t1,t2))
