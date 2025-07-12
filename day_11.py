from collections import Counter

# Read input
with open('data/day11.txt', 'r') as f:
    data = f.read().strip()

# Parse input into list of numbers
numbers = [int(x) for x in data.split()]

def transform_number(num):
    """Apply the transformation rules to a single number"""
    if num == 0:
        return 1
    elif len(str(num)) % 2 == 0:  # Even number of digits
        # Split down the middle
        num_str = str(num)
        mid = len(num_str) // 2
        left = int(num_str[:mid])
        right = int(num_str[mid:])
        return [left, right]
    else:  # Odd number of digits
        return num * 2024

def as_list(x):
    return x if isinstance(x, list) else [x]

def transform_counter(counter):
    new_counter = Counter()    
    for num, count in counter.items():
        transformed = transform_number(num)
        if isinstance(transformed, list): # Split into two numbers
            for item in transformed:
                new_counter[item] += count
        else: # Single number
            new_counter[transformed] += count
    return new_counter

# Part A: 25 iterations
current = Counter(numbers)
for i in range(25):
    current = transform_counter(current)
  
print(f"Part A: {sum(current.values())} after 25 iterations")

# Part B: 75 iterations (reset to initial state)
current = Counter(numbers)
for i in range(75):
    current = transform_counter(current)

print(f"Part B: {sum(current.values())} after 75 iterations") 