#!/usr/bin/env pyton3

import os

this_dir = os.path.dirname(__file__)

with open(this_dir + "/input", mode='r') as file:
    input_ = [int(line.strip()) for line in file.readlines() if line]

# print("\n".join([str(i) for i in input_]))

answer1 = [i for i in input_ if 2020 - i in input_]

answer2 = []
for num1 in input_:
    first_difference = 2020 - num1
    new_candidates = [i for i in input_ if first_difference - i in input_]
    if len(new_candidates) == 2:
        answer2 = (num1, new_candidates[0], new_candidates[1])
        break

print("First part:")
print(answer1)
print(answer1[0] * answer1[1])
print("\nSecond part:")
print(answer2)
print(answer2[0] * answer2[1] * answer2[2])
