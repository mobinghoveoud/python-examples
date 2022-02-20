import re


def totalSeconds(time):
    time = time.split(":")
    return ((int(time[0]) * 60) + int(time[1])) * 60 + int(time[2])


file = open("sample.srt")
sub = file.read()
times = re.findall("([0-9:]{8}),[0-9]{3} --> ([0-9:]{8}),[0-9]{3}", sub)

seconds = 0
for time in times:
    seconds += totalSeconds(time[1]) - totalSeconds(time[0])

print(seconds)
