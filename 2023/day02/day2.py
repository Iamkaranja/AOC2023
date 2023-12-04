#!/usr/bin/env python3

import sys
from collections import defaultdict
from functools import reduce

t = defaultdict(int, {"red": 12, "green": 13, "blue": 14})

with open(sys.argv[1], 'r') as f:
    lines = [l.strip() for l in f.readlines()]

part1 = 0
part2 = 0
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
for line in lines:
    game_str, score_str = line.split(": ")
    game_id = int(game_str.split(" ")[-1])
    p1_game_valid = True
    p2_set = defaultdict(int)
    # r, g, b = 0, 0, 0 # for part 2
    for score in score_str.split("; "):
        for color_str in score.split(", "):
            num_str, color = color_str.split(" ")
            num = int(num_str)
            if t[color] < num:
                p1_game_valid = False
            p2_set[color] = max(p2_set[color], num) # using max to get the max value of the color
            # if color == "red":
            #     r = max(r, num)
            # if color == "blue":
            #     b = max(b, num)
            # if color == "green":
            #     g = max(g, num)
    if p1_game_valid:
        part1 += game_id
    part2 += reduce(lambda x, y: x * y, p2_set.values(), 1)  # using reduce to multiply all values in dict
    # part2  += r * g * b
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
