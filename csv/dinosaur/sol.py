import csv
import math

leglength_map = {}
speed_map = {}
with open("dataset1.csv", "r") as file1:
    file1_reader = csv.reader(file1)
    next(file1_reader)
    for line in file1_reader:
        if line[0] not in leglength_map:
            leglength_map[line[0]] = line[1]

with open("dataset2.csv", "r") as file2:
    file2_reader = csv.reader(file2)
    next(file2_reader)
    for line in file2_reader:
        if line[0] in leglength_map and line[2] == "bipedal":
            ll = float(leglength_map[line[0]])
            sl = float(line[1])
            speed = ((sl / ll) - 1) * math.sqrt(ll * 9.8)
            speed_map[line[0]] = float(speed)

print(sorted(speed_map.items(), key=lambda x: x[1], reverse=True))

dict1 = {}

g = 9.8

with open("dataset2.csv", "r") as csvfile:
    dino2 = csv.reader(csvfile)
    for line in dino2:
        NAME, STRIDE, STANCE = line
        if line[2] == "bipedal":
            dict1[NAME] = float(STRIDE)

with open("dataset1.csv", "r") as csvfile:
    dino1 = csv.reader(csvfile)
    for line in dino1:
        NAME, LEG, DIET = line
        if NAME in dict1:
            STRIDE, LEG = dict1[NAME], float(LEG)
            dict1[NAME] = ((STRIDE / LEG) - 1) * math.sqrt(LEG * g)

output = sorted(dict1.items(), key=lambda i: i[1], reverse=True)
print(output)
for val in output[0:3]:
    print(val[0])
