import re
import numpy as np
input_data = open("input3.txt", "r").read()
wire_1, wire_2 = input_data.split()
wire_1 = wire_1.split(",")
wire_2 = wire_2.split(",")
wire_path_1 = []
wire_path_2 = []
max = 0
for i, elements in enumerate(wire_1):
    wire_1[i] = re.findall(r'(\w+?)(\d+)', wire_1[i])[0]
    wire_path_1.append([wire_1[i][0], int(wire_1[i][1])])

for i, elements in enumerate(wire_2):
    wire_2[i] = re.findall(r'(\w+?)(\d+)', wire_2[i])[0]
    wire_path_2.append([wire_2[i][0], int(wire_2[i][1])])
    if wire_path_1[i][1] > max:
        max = wire_path_1[i][1]

# max = 1000
def build_path(wire):
    hej = 1


