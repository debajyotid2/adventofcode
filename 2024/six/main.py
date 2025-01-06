"""
Advent of code day six
"""
from copy import deepcopy

obstacle = "#"
empty = "."
up = "^"
down = "v"
left = "<"
right = ">"
visited = "X"

def reset_grid(grid: list[list[str]]) -> list[list[str]]:
    for row in grid:
        if visited in row:
            row = row.replace(visited, empty)
    return grid

def find_initial_position(grid: list[list[str]]) -> list[int]:
    for i, row in enumerate(grid):
        j, direc = None, None
        if up in row:
            j = row.index(up)
            direc = up
        elif down in row:
            j = row.index(down)
            direc = down
        elif left in row:
            j = row.index(left)
            direc = left
        elif right in row:
            j = row.index(right)
            direc = right
        if j is not None and direc is not None:    
            return [i, j, direc]

def print_grid(grid: list[list[str]]):
    print()
    for row in grid:
        print("".join(row))
    print()

def part_one(grid: list[list[str]], curr_pos: list[int, int, int]) -> int:
    row, col, direc = curr_pos
    pos_updated = 0
    while True:
        match direc:
            case "^":
                for i in range(row, -1, -1):
                    if grid[i][col] != obstacle:
                        if grid[i][col] != visited:
                            grid[i][col] = visited
                            pos_updated += 1
                        curr_pos[0] -= 1
                    else:
                        curr_pos = [i+1, col, right]
                        break
            case "v":
                for i in range(row, len(grid)):
                    if grid[i][col] != obstacle:
                        if grid[i][col] != visited:
                            grid[i][col] = visited
                            pos_updated += 1
                        curr_pos[0] += 1
                    else:
                        curr_pos = [i-1, col, left]
                        break
            case "<":
                for j in range(col, -1, -1):
                    if grid[row][j] != obstacle:
                        if grid[row][j] != visited:
                            grid[row][j] = visited
                            pos_updated += 1
                        curr_pos[1] -= 1
                    else:
                        curr_pos = [row, j+1, up]
                        break
            case ">":
                for j in range(col, len(grid[0])):
                    if grid[row][j] != obstacle:
                        if grid[row][j] != visited:
                            grid[row][j] = visited
                            pos_updated += 1
                        curr_pos[1] += 1
                    else:
                        curr_pos = [row, j-1, down]
                        break
        row, col, direc = curr_pos
        if (direc == up and row == -1) or \
           (direc == down and row == len(grid)) or \
           (direc == left and col == -1) or \
           (direc == right and col == len(grid[0])):
            return pos_updated
    return 0

def main():
    with open("input", "r") as f:
        initial = f.readlines()
    grid = [list(row) for row in initial]
    initial_grid = deepcopy(grid)

    # Find current position
    curr_pos = find_initial_position(grid)
    
    # Part one
    pos_updated = part_one(grid, curr_pos)
    print(f"Part one answer: {pos_updated}")

if __name__=="__main__":
    main()

