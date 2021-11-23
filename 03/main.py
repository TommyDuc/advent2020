#!/usr/bin/env python3

import os

this_dir = os.path.dirname(__file__)

with open(this_dir + "/input", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]

length = len(input_[0])
height = len(input_)

i = 0
j = 0
tree_count = 0

while True:
    j += 3
    j = j % length
    i += 1

    if i >= height:
        break

    char = input_[i][j]
    if char == "#":
        tree_count += 1

print(tree_count)
