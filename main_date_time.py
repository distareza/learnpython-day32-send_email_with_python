import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()

print(f"now : {now}, year : {year}, month : {month}, day : {day}, day of week : {day_of_week}")

date_of_birth = dt.datetime(year=1995, month=6, day=19, hour=11, minute=23)
print(f"birthday : {date_of_birth}")