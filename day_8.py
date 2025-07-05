from collections import defaultdict
from itertools import combinations

# Read the grid
with open("data/day8.txt") as f:
    grid = [line.strip() for line in f]

def find_non_period_cells(grid):
    """Find all non-period cells and group them by content."""
    groups = defaultdict(list)
    
    for row, line in enumerate(grid):
        for col, cell in enumerate(line):
            if cell != '.':
                groups[cell].append((row, col))
    
    return groups

def find_antinodes(point1, point2):
    """Find antinodes for a pair of points."""
    row1, col1 = point1
    row2, col2 = point2
    
    # Calculate the vector between the two points
    drow = row2 - row1
    dcol = col2 - col1
    
    # Antinodes are at the same distance from one of the points
    # in the opposite direction
    antinode1 = (row1 - drow, col1 - dcol)  # Same distance from point1
    antinode2 = (row2 + drow, col2 + dcol)  # Same distance from point2
    
    return [antinode1, antinode2]

def find_nodes_on_line(point1, point2, grid_size):
    """Find all nodes that lie on the line between two points."""
    row1, col1 = point1
    row2, col2 = point2
    
    nodes = []
    
    # Handle different line types
    if row1 == row2:  # Horizontal line
        # All cells in the same row between the two points
        min_col = min(col1, col2)
        max_col = max(col1, col2)
        for col in range(min_col, max_col + 1):
            nodes.append((row1, col))
    
    elif col1 == col2:  # Vertical line
        # All cells in the same column between the two points
        min_row = min(row1, row2)
        max_row = max(row1, row2)
        for row in range(min_row, max_row + 1):
            nodes.append((row, col1))
    
    else:  # Diagonal line
        # Use Bresenham's line algorithm for robust diagonal line drawing
        dx = abs(col2 - col1)
        dy = abs(row2 - row1)
        
        # Determine step directions
        sx = 1 if col1 < col2 else -1
        sy = 1 if row1 < row2 else -1
        
        # Initialize error
        err = dx - dy
        
        x, y = col1, row1
        
        while True:
            nodes.append((y, x))
            if x == col2 and y == row2:
                break
                
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x += sx
            if e2 < dx:
                err += dx
                y += sy
    
    return nodes

def is_valid_position(pos, grid_size):
    """Check if a position is within the grid bounds."""
    row, col = pos
    return 0 <= row < grid_size and 0 <= col < grid_size

def find_all_antinodes(grid):
    """Find all antinodes for all pairs of like cells."""
    groups = find_non_period_cells(grid)
    grid_size = len(grid)
    all_antinodes = set()  # Use a set to store unique antinodes
    
    for positions in groups.values():
        for p1, p2 in combinations(positions, 2):
            for pos in find_antinodes(p1, p2):
                if 0 <= pos[0] < grid_size and 0 <= pos[1] < grid_size:
                    all_antinodes.add(pos)
    
    return all_antinodes

def find_all_collinear_nodes(grid):
    """Find all grid cells collinear with any pair of like cells (including the original two points)."""
    groups = find_non_period_cells(grid)
    grid_size = len(grid)
    all_nodes = set()

    for positions in groups.values():
        for (r1, c1), (r2, c2) in combinations(positions, 2):
            for r in range(grid_size):
                for c in range(grid_size):
                    # Check collinearity (now including the original points)
                    if (r2 - r1) * (c - c1) == (c2 - c1) * (r - r1):
                        all_nodes.add((r, c))
    return all_nodes

# Run the analysis
antinodes = find_all_antinodes(grid)
print(f"Part A Answer: {len(antinodes)} Nodes")

collinear_nodes = find_all_collinear_nodes(grid)
print(f"Part B Answer: {len(collinear_nodes)} Nodes") 