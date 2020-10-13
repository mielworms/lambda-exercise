import datetime
now = datetime.datetime.now()
print(now)
year = lambda a: a.year
month = lambda a: a.month
day = lambda a: a.day
t = lambda a: a.time()
print(year(now))
print(month(now))
print(day(now))
print(t(now))