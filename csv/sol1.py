import math

dinos1 = {}
dinos2 = {}
ans = []
csv1 = open("1.csv", "r")
csv2 = open("2.csv", "r")
csv1_lines = csv1.readlines()
csv2_lines = csv2.readlines()
g = 9.8
for line in csv2_lines:
    NAME, SL, STANCE = line.strip().split(",")
    if STANCE == "bipedal":
        dinos2[NAME] = {"sl": float(SL), "stance": STANCE}
print(dinos2)
for line in csv1_lines:
    NAME, LL, DIET = line.split(",")
    if NAME in dinos2:
        dinos2[NAME]["speed"] = (((dinos2[NAME]["sl"]) / float(LL)) - 1) * math.sqrt(
            float(LL) * g
        )
print(dinos2.items())
