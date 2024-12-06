import re

# Load data, then make it all one string instead of multiple entries
file = open("data/day3.txt").readlines()
file_combined = ''.join(file)

# Regular expression to find mul(A,B) where A,B are both numbers
pattern = r"mul\(\d*,\d*\)"

data = re.findall(pattern, file_combined)

# Runs the mul(A,B) function appropriately
def multiplier(string): 
    a,b = string.replace('mul(', '').replace(')','').split(',')
    score = int(a) * int(b) 
    return score 

score = 0
for entry in data:
    score += multiplier(entry)

print("Part A: " + str(score))

#### Onto Part B ####

# New option with three patterns separat
patterns = r"mul\(\d*,\d*\)|do\(\)|don\'t\(\)"

data = re.findall(patterns, file_combined)

score = 0
switch = True
for entry in data:
    if entry == "don't()":
        switch = False
    if entry == "do()":
        switch = True
    elif switch == True: 
        score += multiplier(entry)

print("Part B: " + str(score))
