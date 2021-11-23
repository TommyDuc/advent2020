#!/usr/bin/env python3

import os

this_dir = os.path.dirname(__file__)

with open(this_dir + "/input", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]

length = len(input_[0])
height = len(input_)

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]


def count_trees(slope):
    right = slope[0]
    down = slope[1]
    i = 0
    j = 0
    tree_count = 0

    while True:
        j += right
        j = j % length
        i += down

        if i >= height:
            break

        char = input_[i][j]
        if char == "#":
            tree_count += 1

    return tree_count


counts = [count_trees(slope) for slope in slopes]
product = 1
for count in counts:
    product *= count

print(counts)
print(product)
