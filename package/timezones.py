from datetime import datetime
import pytz


def totalSeconds(time):
    time = time.split(":")
    return ((int(time[0]) * 60) + int(time[1])) * 60 + int(time[2])


inputTime = totalSeconds(input())

min = 60*60*24
minTimeZone = ""

for tzone in pytz.all_timezones:
    nowTime = datetime.now(pytz.timezone(tzone)).strftime("%H:%M:%S")
    cTime = abs(inputTime - totalSeconds(nowTime))
    if (cTime < min):
        min = cTime
        minTimeZone = tzone

print(minTimeZone)
