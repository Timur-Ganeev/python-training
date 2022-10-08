import time
import os
import pandas

delayTime = 10
sensFilePath = "data/sensor.csv"

print(f"Start file processing: {sensFilePath} ->")

if os.path.exists(sensFilePath):
    while True:
        if os.path.exists(sensFilePath):
            sensData = pandas.read_csv(sensFilePath)
            print(sensData.mean())

            print(f"Wait {delayTime} sec.")
            time.sleep(delayTime)
        else:
            print(f"File was deleted during operation: '{sensFilePath}'")
            break
else:
    print(f"File don't exist: '{sensFilePath}'")

print(f"End file processing: {sensFilePath}")
