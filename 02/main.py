#!/usr/bin/env python3

import re
import os

this_dir = os.path.dirname(__file__)

with open(this_dir + "/input", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]

good_password_count1 = 0
for line in input_:
    password_policy_expression = re.compile(r'^(\d+)-(\d+) (\w): (\w+)')
    match = password_policy_expression.match(line)

    if not match:
        break

    groups = match.groups()
    lower = int(groups[0])
    upper = int(groups[1])
    character = groups[2]
    password = groups[3]

    if lower <= password.count(character) <= upper:
        good_password_count1 += 1

good_password_count2 = 0
for line in input_:
    password_policy_expression = re.compile(r'^(\d+)-(\d+) (\w): (\w+)')
    match = password_policy_expression.match(line)

    if not match:
        break

    groups = match.groups()
    lower = int(groups[0]) - 1
    upper = int(groups[1]) - 1
    character = groups[2]
    password = groups[3]

    if (password[lower] == character) ^ (password[upper] == character):
        good_password_count2 += 1

print("First part:")
print(good_password_count1)
print("\nSecond part:")
print(good_password_count2)

