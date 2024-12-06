with open("data/day2.txt") as file: 
    data = [list(map(int, line.split())) for line in file]

def all_increasing(entry): 
    check = True
    for x,y in zip(entry[:-1], entry[1:]):
        if (y <=  x):
            check = False
    return check 

def all_decreasing(entry): 
    check = True
    for x,y in zip(entry[:-1], entry[1:]):
        if (y >=  x):
            check = False
    return check 

def safe_distance(entry):
    check = True
    for x,y in zip(entry[:-1], entry[1:]):
        if abs(y - x) > 3 or x == y:
            check = False
    return check 

safe_entries = 0

for report in data: 
    if (all_increasing(report) or all_decreasing(report)) and safe_distance(report): 
        safe_entries += 1

print("Part A: " + str(safe_entries))

#########

safe_entries = 0 

for report in data: 
    if ((all_increasing(report) or all_decreasing(report)) and safe_distance(report)): 
        safe_entries += 1
        
    else:
        minisafe = 0 
        levels = len(report)
        for i in range(levels): 
            minireport = report[:i]+report[i+1:]
            if (all_increasing(minireport) or all_decreasing(minireport)) and safe_distance(minireport): 
                minisafe += 1
        if minisafe > 0: 
            safe_entries += 1

print("Part B: " + str(safe_entries))