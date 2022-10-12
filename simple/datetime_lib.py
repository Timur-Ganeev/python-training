from datetime import datetime, timedelta, timezone
import time
# import pytz

data = [['5.10.2016 10:11', 0.01, 0.02, None], ['6.10.2016T 10:00', 0.2, 0.24, 0.68], ['7.10.16 10:12', 0.11, 0.37, None], ['8.10.2016T 10:08', 0.01, 0.04, 0.33]]
print(data[0][0])
date_val = datetime.strptime(data[0][0], '%d.%m.%Y %H:%M')
print(date_val)
print(datetime.now())
print(datetime(year=2024, month=1, day=29))
print(datetime.strptime("May 25 2017 5:00AM", "%b %d %Y %I:%M%p"))
print(datetime.strptime("May 25 2017 5:00PM", "%b %d %Y %I:%M%p"))

date_format = "%Y-%m-%d"
start_date = "2018-01-01"   # "%Y-%m-%d" при таком формате даты идут в алфавитном порядке
end_date = "2018-01-07"

print("2018-01-01" < "2018-01-05")

start_dt = datetime.strptime(start_date, date_format)
end_dt = datetime.strptime(end_date, date_format)

print(f"Days: {(end_dt - start_dt).days}")

print(start_dt + timedelta(days=1, minutes=90))
print(start_dt + timedelta(days=1, minutes=-90))
print(datetime.strptime("2018-09-01T09:30:00", "%Y-%m-%dT%H:%M:%S") + timedelta(hours=12, minutes=15, seconds=3))

print(end_dt.strftime("%Y-%m-%d"))
print("---")

cur_dt = start_dt
while cur_dt <= end_dt:
    print(cur_dt)
    # cur_dt += timedelta(days=1)
    cur_dt += timedelta(hours=12)

day_of_month = datetime.strptime("2018-01-01", date_format).day
print(day_of_month)
day_from_str = "2018-01-01"[8:10]   # преобразования дат тяжелые, так в разы быстрее
print(int(day_from_str))

# unixtime
offset = datetime(year=1970, month=1, day=1, tzinfo=timezone.utc)
dt = datetime.now(tz=timezone.utc)
print(dt)
ut_sec = time.mktime(dt.timetuple())
print(ut_sec)
print(datetime.fromtimestamp(0, tz=timezone.utc))