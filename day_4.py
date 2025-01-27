import numpy as np
from itertools import product

file = open('data/day4.csv').readlines()
data = np.array([list(line.strip()) for line in file])

# Part 1 Checking and Scoring
def check_side(df):
    score = 0
    for i in range(data.shape[0]):
        score += sum("".join(df[i,j:j+4])=='XMAS' for j in range(df.shape[1]-3))
    return score 

def check_cols(df):
    score = 0
    for j in range(data.shape[1]):
        score += sum("".join(df[i:i+4,j])=='XMAS' for i in range(df.shape[0]-3))
    return score 

def check_diag(df):
    score = 0
    for i,j in product(range(data.shape[0] -3), range(data.shape[1]-3)):
        if (df[i,j] + df[i+1,j+1] + df[i+2,j+2] + df[i+3,j+3]) == 'XMAS':
            score += 1
    return score 

total = 0 
total += check_side(data)
total += check_side(np.fliplr(data))
total += check_cols(data)
total += check_cols(np.flipud(data))
total += check_diag(data)
total += check_diag(np.fliplr(data))
total += check_diag(np.flipud(data))
total += check_diag(np.fliplr(np.flipud(data)))

print("Part 1: " + str(total)) 

# Part 2 - looking for MAS crosses: 
def find_crosses(df):
    score = 0
    
    for i,j in product(range(1, data.shape[0] -1), range(1, data.shape[1]-1)):
        if df[i,j] == 'A': 
            if ((df[i-1,j-1] + df[i,j] + df[i+1,j+1]) == 'MAS')|((df[i-1,j-1] + df[i,j] + df[i+1,j+1]) == 'SAM'):
                if ((df[i+1,j-1] + df[i,j] + df[i-1,j+1]) == 'MAS')|((df[i+1,j-1] + df[i,j] + df[i-1,j+1]) == 'SAM'):
                    score += 1
    return score 

score2 = find_crosses(data)

print("Part 2: " + str(score2))

