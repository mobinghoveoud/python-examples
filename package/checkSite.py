import time
import requests

url = "https://www.time.ir/"
r = requests.get(url)
preText = r.text
time.sleep(10)

while True:
    r = requests.get(url)
    if (preText != r.text):
        print("Changed!")

    preText = r.text
    time.sleep(10)
