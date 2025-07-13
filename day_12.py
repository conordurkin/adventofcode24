from collections import deque, defaultdict

filename = 'data/day12test.txt'

with open(filename, 'r') as f:
    data = [line.strip() for line in f if line.strip()]

def solve_part_a(data):
    nrows, ncols = len(data), len(data[0])
    visited = [[False]*ncols for _ in range(nrows)]
    regions = []
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    for r in range(nrows):
        for c in range(ncols):
            if not visited[r][c]:
                letter = data[r][c]
                queue = deque([(r, c)])
                visited[r][c] = True
                area = 0
                perimeter = 0
                while queue:
                    cr, cc = queue.popleft()
                    area += 1
                    for dr, dc in directions:
                        nr, nc = cr+dr, cc+dc
                        if 0 <= nr < nrows and 0 <= nc < ncols:
                            if data[nr][nc] == letter:
                                if not visited[nr][nc]:
                                    visited[nr][nc] = True
                                    queue.append((nr, nc))
                            else:
                                perimeter += 1
                        else:
                            perimeter += 1
                regions.append({'letter': letter, 'area': area, 'perimeter': perimeter})
    # Calculate the sum of area * perimeter for all regions
    return sum(reg['area'] * reg['perimeter'] for reg in regions)


def solve_part_b(data):
# TBD - Haven't solved so far! 
 
print(f"Part A: {solve_part_a(data)}")
print(f"Part B: {solve_part_b(data)}") 