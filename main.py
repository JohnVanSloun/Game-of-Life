grid = [[0 for i in range(25)] for j in range(25)]
DEAD = 0
LIVE = 1

# Resets the grid state to its initial state
def reset_grid():
    grid = [[0 for i in range(25)] for j in range(25)]

# Updates a cell at the specified x, y index pair to value
def update_cell(x, y, value):
    grid[x][y] = value

# Prints the current state of the grid to standard output
def print_grid():
    row_len = len(grid[0])
    col_len = len(grid)

    for i in range(col_len):
        for j in range(row_len):
            if j == row_len - 1:
                print(grid[i][j])
            else:
                print(grid[i][j], end="")