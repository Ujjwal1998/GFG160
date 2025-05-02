import random

with open("log.log", "r") as log:
    read_log = log.read()
    logs = read_log.split("%")
    print(logs)
    r = random.randint(0, len(logs) - 1)
    print(logs[r])
