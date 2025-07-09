from collections import deque

# Read the grid from file at the top
with open('data/day10.txt') as f:
    grid = [list(map(int, line.strip())) for line in f]

rows = len(grid)
cols = len(grid[0]) if grid else 0

def find_zeros(grid):
    zeros = []
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == 0:
                zeros.append((r, c))
    return zeros

def reachable_nines(grid, start):
    visited = set()
    nines = set()
    queue = deque()
    queue.append((start[0], start[1], grid[start[0]][start[1]]))  # (row, col, current_value)
    visited.add((start[0], start[1]))
    while queue:
        r, c, val = queue.popleft()
        if val == 9:
            nines.add((r, c))
            continue  # Don't search further from a 9
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited and grid[nr][nc] == val + 1:
                    visited.add((nr, nc))
                    queue.append((nr, nc, grid[nr][nc]))
    return nines

# Main script logic
zeros = find_zeros(grid)
summary = []
for zero_pos in zeros:
    nines = reachable_nines(grid, zero_pos)
    summary.append((zero_pos, len(nines)))

# Sum the total number of 9s that can be reached from all 0s (counting duplicates)
total_nines_reached = sum(count for pos, count in summary)
print(f"Part A: {total_nines_reached}")

# --- Part B: Count distinct paths from each 0 to any 9 ---
def count_paths_to_nines(grid, start):
    rows = len(grid)
    cols = len(grid[0]) if grid else 0
    def dfs(r, c, val, visited):
        if val == 9:
            return 1
        total = 0
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited and grid[nr][nc] == val + 1:
                    total += dfs(nr, nc, grid[nr][nc], visited | {(nr, nc)})
        return total
    return dfs(start[0], start[1], grid[start[0]][start[1]], {start})

b_summary = []
for zero_pos in zeros:
    num_paths = count_paths_to_nines(grid, zero_pos)
    b_summary.append((zero_pos, num_paths))

total_paths = sum(count for pos, count in b_summary)
print(f"Part B: {total_paths}") 

