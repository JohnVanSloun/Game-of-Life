grid_state = [[0 for i in range(100)] for j in range(100)]
DEAD = 0
LIVE = 1

def reset_grid():
    grid_state = [[0 for i in range(100)] for j in range(100)]

def update_cell(x, y, value):
    grid_state[x][y] = value

def print_grid():
    row_len = 100
    col_len = 100

    for i in range(col_len):
        for j in range(row_len):
            if j == row_len - 1:
                print(grid[i][j] + "\n")
            else:
                print(grid[i][j])