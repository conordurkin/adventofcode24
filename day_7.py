import itertools

with open("data/day7.txt") as f:
    lines = [line.strip() for line in f if line.strip()]

def sum_successful_goals(lines):
    successes = 0
    for line in lines:
        goal_str, values_str = line.split(':')
        goal = int(goal_str.strip())
        values = list(map(int, values_str.strip().split()))
        n = len(values)
        if n == 1:
            if values[0] == goal:
                successes += goal
            continue
        # Generate all possible combinations of + and *
        for ops in itertools.product(['+', '*'], repeat=n-1):
            result = values[0]
            for i, op in enumerate(ops):
                if op == '+':
                    result += values[i+1]
                else:
                    result *= values[i+1]
            if result == goal:
                successes += goal
                break  # Only count each row once
    print(f"Part A: {successes}")
    return successes

def sum_successful_goals_v2(lines):
    successes = 0
    for line in lines:
        goal_str, values_str = line.split(':')
        goal = int(goal_str.strip())
        values = list(map(int, values_str.strip().split()))
        n = len(values)
        if n == 1:
            if values[0] == goal:
                successes += goal
            continue
        # Now allow '+', '*', and 'concat' as operations
        for ops in itertools.product(['+', '*', 'concat'], repeat=n-1):
            result = values[0]
            for i, op in enumerate(ops):
                if op == '+':
                    result += values[i+1]
                elif op == '*':
                    result *= values[i+1]
                elif op == 'concat':
                    # Concatenate as strings, then convert back to int
                    result = int(str(result) + str(values[i+1]))
            if result == goal:
                successes += goal
                break
    print(f"Part B: {successes}")
    return successes

sum_successful_goals(lines)
sum_successful_goals_v2(lines) 