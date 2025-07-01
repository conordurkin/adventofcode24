import numpy as np
file = open('data/day6.txt').readlines()
data = np.array([list(line.strip()) for line in file])

# Okay so we've got this big array to traverse around. 

# The guard is still in the grid, so he hasn't escaped yet. 
escaped = False

# Current direction is 'North,'
direction = np.array([-1,0])

# Find the starting position denoted by the ^ symbol 
position = np.argwhere(data == '^')[0]

# So long as we haven't recorded an escape, first check to see if our current position is "off the grid." If so we escaped.
while escaped == False:
    row,col = position 
    if ((row < 0) or (row == len(data)) or (col < 0) or (col == len(data[0]))):
        escaped = True 

    # Otherwise, let's try to take a step in our current direction 
    new_row, new_col = position + direction 

    try:
        # If we hit an obstacle, instead we'll turn to the right (N > E > S > W > N) but not move. 
        if data[new_row][new_col] == '#':
            direction = [direction[1], -direction[0]]
        # If we don't hit an obstacle, we mark our current position with @, then move forward one step. 
        # Then we update our current position accordingly. 
        else:
            data[row][col] = '@'
            data[new_row][new_col] = '^'
            position = np.array([new_row, new_col])
    
    # If we can't step forward - because it'd be an escape - then we mark our current position and escape.
    except:
        data[row][col] = '@'
        escaped = True

score = (np.sum(data == '@'))

print("Part A: "+str(score))

# Part 2 - I'm gonna brute force it. If you haven't escaped after 10k steps, I'm assuming you're stuck. 

# Reload the data to get it fresh. 
data = np.array([list(line.strip()) for line in file])
score = 0

# Get rows and cols to loop over, then try every new board one at a time. 
# If you don't escape in 10k steps, you're stuck. 
# Then print how many times we got stuck. 
rows,cols = data.shape
for i in range(rows):
    for j in range(cols):
        new_data = data.copy()
        if new_data[i][j] == '#':
            continue
        if new_data[i][j] == '^':
            continue
        new_data[i][j] = '#' 

        escaped = False
        direction = np.array([-1,0])
        position = np.argwhere(new_data == '^')[0]
        while escaped == False:
            for step in range(10000):
                row,col = position 
                if ((row < 0) or (row == len(new_data)) or (col < 0) or (col == len(new_data[0]))):
                    escaped = True 
                    break
                new_row, new_col = position + direction 
                try:
                    if new_data[new_row][new_col] == '#':
                        direction = [direction[1], -direction[0]]
                    else:
                        new_data[row][col] = '@'
                        new_data[new_row][new_col] = '^'
                        position = np.array([new_row, new_col])
                except:
                    new_data[row][col] = '@'
                    escaped = True
                    break 
            if escaped == False:
                score += 1
                break

print("Part B: "+str(score))