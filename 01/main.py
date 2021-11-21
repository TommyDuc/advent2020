#!/usr/bin/env pyton3

import os

this_dir = os.path.dirname(__file__)

input_ = list()
with open(this_dir + "/input", mode='r') as file:
    input_ = [int(line.strip()) for line in file.readlines()]

# print("\n".join([str(i) for i in input_]))

found_candidates = [i for i in input_ if 2020 - i in input_]
print(found_candidates)
print(found_candidates[0]*found_candidates[1])

