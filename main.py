DEAD = 0
LIVE = 1

grid = [[DEAD for i in range(25)] for j in range(25)]
cells_to_change = []

# Resets the grid state to its initial state
def reset_grid():
    grid = [[DEAD for i in range(25)] for j in range(25)]

# Updates a cell at the specified x, y index pair to value
def update_cell(row, col, value):
    grid[row][col] = value

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

# Counts the number of neighbor cells that are LIVE and returns the count
def num_live_neighbors(row, col):
    num_live = 0

    neighbors = [[row - 1, col], [row - 1, col - 1], [row - 1, col + 1], 
                 [row, col - 1], [row, col + 1], 
                 [row + 1, col], [row + 1, col - 1], [row + 1, col + 1]]

    for neighbor in neighbors:
        if neighbor[0] >= 0 and neighbor[0] < len(grid[row]) and neighbor[1] >= 0 and neighbor[1] < len(grid):
            num_live += grid[neighbor[0]][neighbor[1]]

    return num_live

# Implements rules to decide if a cell should live or die
# Rules:
# 1. If fewer than 2 neighbor cells are LIVE then DEAD
# 2. If cell is LIVE and 2 or 3 neighbor cells are LIVE then LIVE
# 3. If cell is LIVE and more than 3 neighbors are LIVE then DEAD
# 4. If cell is DEAD and 3 neighbor cells are LIVE then LIVE
# Returns True if a change is warranted based on the rules and False otherwise
def check_cell_state(row, col):
    if grid[row][col] == LIVE:
        if num_live_neighbors(row, col) < 2 or num_live_neighbors(row, col) > 3:
            return True
    else:
        if num_live_neighbors(row, col) == 3:
            return True

    return False

# Update all cells in the cells_to_change list
def change_cells():
    for cell in cells_to_change:
        if grid[cell[0]][cell[1]] == DEAD:
            update_cell(cell[0], cell[1], LIVE)
        else:
            update_cell(cell[0], cell[1], DEAD)
