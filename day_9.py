# Read input data
with open("data/day9.txt") as f:
    data = [line.strip() for line in f]

# Part A solution
parsed_data = []
for index, value in enumerate(data[0]):
    if index % 2 == 0:
        parsed_data += [(index // 2)] * int(value)
    else:
        parsed_data += ['.'] * int(value) 

while '.' in parsed_data:
    last_entry = parsed_data.pop() 
    if last_entry == '.':
        continue 
    else: 
        first_period = parsed_data.index('.')
        parsed_data[first_period] = last_entry

result = 0 
for i, v in enumerate(parsed_data):
    result += int(v) * i 

print("Part A Answer:", result) 

# Part B solution
blocks = []
for index, value in enumerate(data[0]):
    if index % 2 == 0:
        blocks += [[(index // 2)] * int(value)]
    else:
        blocks += [['.'] * int(value)]


for entry in range(len(blocks)-1, -1, -1):
    block = blocks[entry]
    if '.' in block: 
        continue  
    if block == []: 
        continue 

    block_size = len(block)
    for spot in range(entry):
        landing = blocks[spot] 
        if '.' not in landing: 
            continue 
        if spot >= entry:
            continue 
        
        landing_size = len(landing)
        if landing_size == block_size: 
            blocks[entry] = ['.'] * block_size
            blocks[spot] = block 
            break 

        if landing_size > block_size: 
            blocks[entry] = ['.'] * block_size
            blocks[spot] = block 
            blocks.insert(spot+1, ['.'] * (landing_size - block_size))
            break 

final_blocks = [entry for block in blocks for entry in block]

result = 0
for i, v in enumerate(final_blocks):
    if isinstance(v, int):
        result += int(v) * i 

print("Part B Answer:", result) 
