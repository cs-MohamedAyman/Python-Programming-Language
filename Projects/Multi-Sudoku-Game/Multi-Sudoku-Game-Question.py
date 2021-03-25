import random
import utils

root_N = 3
N = root_N * root_N
mode = 0
similar_boxes, n_grids = [], []
grids, cpy_grids = [], []

#This function checks if the given grid has a win state or not
def check_win_grid(grid_idx):
    pass

#This function checks if the game has a win state or not
def check_win():
    for grid_idx in range(n_grids[mode]):
        if not check_win_grid(grid_idx):
            return False
    return True

#This function checks if the given position is valid or not 
def check_valid_position(i, j):
    pass

#This function checks if the given grid index is valid or not 
def check_valid_grid_index(grid_idx):
    pass

#This function checks if the given cell is original or not
def check_original_cell(grid_idx, i, j):
    pass

#This function checks if the given value is valid with the given cell
def check_valid_value(grid_idx, i, j, v):
    pass

#This function converts the given position in the grid into a box number
def cvt_grid_pos_to_box(i, j):
    pass

#This function converts the given box number into a position index in the grid
def cvt_box_to_grid_pos(x):
    pass

#This function copies a cell from the givne source grid to the given target grid
def check_valid_value_cell(grid_idx_s, box_idx_s, grid_idx_t, box_idx_t, i, j, v):
    pass

#This function checks if the given value is valid with the shared boxes in the other grids
def check_valid_value_in_shared_boxes(grid_idx, i, j, v):
    pass

#This function copies a cell from the givne source grid to the given target grid
def cpy_cell(grid_idx_s, box_idx_s, grid_idx_t, box_idx_t, i, j, set_original=False):
    pass

#This function copies the shared boxes in the other grids
def cpy_cell_in_shared_boxes(grid_idx, i, j, v):
    for grid_i, box_i, grid_j, box_j in similar_boxes[mode]:
        if grid_idx == grid_i:
            cpy_cell(grid_i, box_i, grid_j, box_j, i, j)
        if grid_idx == grid_j:
            cpy_cell(grid_j, box_j, grid_i, box_i, i, j)

#This function sets the given value to the given cell
def set_cell(grid_idx, i, j, v):
    pass

#This function gets the similar boxes the other grids
def get_similar_boxes(grid_idx, box_idx):
    pass

#This function copies the given box in the shared boxes in the other grids
def cpy_box_in_shared_boxes(grid_idx, box_idx, shared_boxes, set_original=False):
    pass

#This function checks if the given box is empty or not
def is_empty_box(grid_idx, box_idx):
    pass

#This function checks if the given box is divided into empty cells and non-empty cells or not
def is_half_box(grid_idx, box_idx):
    pass

#This function copies the all boxes of the given grid in the shared boxes in the other grids
def cpy_similar_boxes(grid_idx):
    for i in range(0, N, root_N):
        for j in range(0, N, root_N):
            box_idx = cvt_grid_pos_to_box(i, j)
            shared_boxes = get_similar_boxes(grid_idx, box_idx)
            cpy_box_in_shared_boxes(grid_idx, box_idx, shared_boxes, True)

#This function solves the grid
def solve_grid(grid_idx, i, j):
    if j == N:
        i += 1
        j = 0
    if i == N:
        return True
    if check_original_cell(grid_idx, i, j):
        return solve_grid(grid_idx, i, j+1)
    for k in range(1, N+1):
        if check_valid_value_in_shared_boxes(grid_idx, i, j, k):
            grids[grid_idx][i][j] = k
            cpy_grids[grid_idx][i][j] = k
            if solve_grid(grid_idx, i, j+1):
                return True
            grids[grid_idx][i][j] = 0
            cpy_grids[grid_idx][i][j] = 0
    return False

#This function generates cells in the grids
def generate_cells(grid_idx=0):
    for k in range(0, N, root_N):
        box_idx = cvt_grid_pos_to_box(k, k)
        if not is_empty_box(grid_idx, box_idx):
            continue
        for i in range(root_N):
            for j in range(root_N):
                n = random.randint(1, N)
                while not check_valid_value_in_shared_boxes(grid_idx, k+i, k+j, n) or \
                      check_original_cell(grid_idx, k+i, k+j):
                    n = random.randint(1, N)
                grids[grid_idx][k+i][k+j] = n
                cpy_grids[grid_idx][k+i][k+j] = n

#This function removes cells in the grids
def remove_cells(grid_idx=0):
    for k in range((N+1)//2):
        for i in range(0, N, root_N):
            for j in range(0, N, root_N):
                box_idx = cvt_grid_pos_to_box(i, j)
                if is_half_box(grid_idx, box_idx):
                    continue
                t1 = random.randint(0, root_N-1)
                t2 = random.randint(0, root_N-1)
                while not check_original_cell(grid_idx, i+t1, j+t2):
                    t1 = random.randint(0, root_N-1)
                    t2 = random.randint(0, root_N-1)
                grids[grid_idx][i+t1][j+t2] = 0
                cpy_grids[grid_idx][i+t1][j+t2] = 0

#This function generates cells in the given grid
def generate_grids():
    #Generate cells in the grid
    generate_cells()
    for grid_idx in range(n_grids[mode]):
        #Solve the complete grid
        solve_grid(grid_idx, 0, 0)
        #Copy the similar boxes in the another grids
        cpy_similar_boxes(grid_idx)
    for grid_idx in range(n_grids[mode]):
        #Remove cells in the grid to be solved
        remove_cells(grid_idx)
        #Copy the similar boxes in the another grids
        cpy_similar_boxes(grid_idx)

#This function updates the global variables from utils module
def update_vars():
    global root_N, N, mode, similar_boxes, n_grids, grids, cpy_grids
    root_N = utils.root_N
    N = utils.N
    mode = utils.mode
    similar_boxes, n_grids = utils.similar_boxes, utils.n_grids
    grids, cpy_grids = utils.grids, utils.cpy_grids

#This function reads a valid position and value inputs
def read_input():
    grid_idx, i, j, v = map(int, input('Enter the row index and column index and value: ').split())
    while not check_valid_grid_index(grid_idx) or not check_valid_position(i, j) or \
          not check_valid_value_in_shared_boxes(grid_idx, i, j, v) or check_original_cell(grid_idx, i, j):
        grid_idx, i, j, v = map(int, input('Enter a valid row index and column index and value: ').split())
    return grid_idx, i, j, v


#MAIN FUNCTION
def play_game():
    print("Multi-Sudoku Game!")
    print("Welcome...")
    print("============================")
    while True:
        #Prints the grids
        utils.print_grids()
        #Read an input from the player
        grid_idx, i, j, v = read_input()
        #Set the input position with the value
        set_cell(grid_idx, i, j, v)
        #Check if the grid has a win state
        if check_win():
            #Prints the grids
            utils.print_grids()
            #Announcement of the final statement
            print('Congrats, You won!')
            break

while True:
    utils.contract_modes()
    utils.print_modes()
    utils.set_config()
    utils.grid_clear()
    update_vars()
    generate_grids()
    play_game()
    c = input('Play Again [Y/N] ')
    if c not in 'yY':
        break
