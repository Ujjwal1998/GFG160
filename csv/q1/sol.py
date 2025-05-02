import csv

ans = {}
ingress_map = {}
with open("interface_ingress.csv", "r") as ingress_file:
    ingress_reader = csv.reader(ingress_file)
    next(ingress_reader)
    ingress_reader = list(ingress_reader)
    for line in ingress_reader:
        interface = line[0]
        bytes_in = line[2]
        ingress_map[interface] = bytes_in

with open("interface_egress.csv", "r") as egress_file:
    egress_reader = csv.reader(egress_file)
    next(egress_reader)
    egress_reader = list(egress_reader)
    i = 0
    for line in egress_reader:
        interface = line[0]
        bytes_out = line[2]
        i += 1
        if interface in ingress_map:
            imbalance = abs(int(ingress_map[interface]) - int(bytes_out))
            ans[interface] = (imbalance, i)
for interface in sorted(ans.items(), key=lambda x: x[1][1], reverse=True):
    print(interface, ans[interface[0]])
