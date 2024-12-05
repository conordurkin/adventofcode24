import pandas as pd
data = pd.read_csv('data/day1.csv', sep='\\s+', header=None)

left = data[0].tolist()
right = data[1].tolist()

left.sort()
right.sort()

dist = 0
for i in range(len(left)): 
    dist += abs(left[i] - right[i])

print("Part A: " + str(dist))

#########

score = 0 
for entry in left:
    score += right.count(entry) * entry 
print("Part B: " + str(score))