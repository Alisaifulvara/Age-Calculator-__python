#Write a program to determine how many number of days a person have survived since his/her birth
import datetime
from datetime import date
year=int(input("birth year: "))
month=int(input("birth month: "))
day=int(input("birth day: "))

date1 = date(year,month,day)


print("Birth date is: ",date1)

y=int(input("current year: "))
m=int(input("current month: "))
d=int(input("current day: "))
date2= date(y,m,d)

print("Current date is:",date2)

print("number of days you have survived are:",date2-date1)