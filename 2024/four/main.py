"""
Advent of code day four
"""

def print_grid(grid: list[str]):
    for line in grid:
        print(line)

def search(grid: list[str]) -> int:
    count = 0
    for line in grid:
        count += line.count("XMAS") + line.count("SAMX")
    return count

def transpose(grid: list[str]) -> list[str]:
    transposed = []
    for i in range(len(grid[0])):
        transposed.append("".join([row[i] for row in grid]))
    return transposed

def left_diagonals(grid: list[str]) -> list[str]:
    diags = []
    i, j = 0, 0
    while i < len(grid):
        curr = []
        loc_i = i
        j = 0
        while loc_i >= 0 and j < len(grid[0]):
            curr.append(grid[loc_i][j])
            loc_i -= 1
            j += 1
        diags.append("".join(curr))
        i += 1
    j = 1
    while j < len(grid):
        curr = []
        i = len(grid)-1
        loc_j = j
        while i > 0 and loc_j < len(grid[0]):
            if grid[i][loc_j] != "\n":
                curr.append(grid[i][loc_j])
            i -= 1
            loc_j += 1
        diags.append("".join(curr))
        j += 1
    return diags

def right_diagonals(grid: list[str]) -> list[str]:
    diags = []
    i, j = len(grid)-1, len(grid)-1
    while j >= 0:
        curr = []
        i = 0
        loc_j = j
        while i < len(grid) and loc_j < len(grid[0]):
            if grid[i][loc_j] != "\n":
                curr.append(grid[i][loc_j])
            i += 1
            loc_j += 1
        diags.append("".join(curr))
        j -= 1
    i = 1
    while i < len(grid):
        curr = []
        loc_i = i
        j = 0
        while loc_i < len(grid) and j < len(grid[0]):
            curr.append(grid[loc_i][j])
            loc_i += 1
            j += 1
        diags.append("".join(curr))
        i += 1
    return diags

def tile_search(grid: list[str]) -> int:
    count = 0
    for i in range(len(grid)-2): 
        for j in range(len(grid[0])-3):
            diag_1 = "".join([grid[i][j], grid[i+1][j+1], grid[i+2][j+2]])
            diag_2 = "".join([grid[i+2][j], grid[i+1][j+1], grid[i][j+2]])
            if (diag_1 == "SAM" or diag_1 == "MAS") and \
                (diag_2 == "SAM" or diag_2 == "MAS"):
                count += 1
    return count

def main():
    with open("input", "r") as f:
        grid = f.readlines()

    # Part one
    count = search(grid) + search(transpose(grid)) + search(left_diagonals(grid)) + search(right_diagonals(grid))
    print(f"Part one answer: {count}")

    # Part two
    count = tile_search(grid)
    print(f"Part two answer: {count}")

if __name__=="__main__":
    main()
