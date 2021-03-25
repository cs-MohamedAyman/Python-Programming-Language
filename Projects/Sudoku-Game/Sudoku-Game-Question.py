import random
root_N = 3
N = root_N * root_N
grid, cpy_grid = [], []
symbols = ['.', '1', '2', '3', '4', '5', '6', '7', \
           '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G']

#This function prints the grid of Sudoku Game as the game progresses
def print_grid():
    print(('-' * (N*3)) + ('---' * root_N) + '-')
    for i in range(N):
        print(end='|  ')
        for j in range(N):
            if j % root_N == 0 and j > 0:
                print('|  ', end='')
            print(symbols[grid[i][j]], end='  ')
        print(end='|')
        print()
        if i % root_N == root_N - 1:
            print(('-' * (N*3)) + ('---' * root_N) + '-')

#This function checks if the game has a win state or not
def check_win():
    pass

#This function checks if the given position is valid or not 
def check_valid_position(i, j):
    pass

#This function checks if the given cell is original or not
def check_original_cell(i, j):
    pass

#This function checks if the given value is valid with the given cell
def check_valid_value(i, j, v):
    pass

#This function sets the given value to the given cell
def set_cell(i, j, v):
    pass

#This function solves the grid
def solve_grid(i, j):
    if j == N:
        i += 1
        j = 0
    if i == N:
        return True
    if check_original_cell(i, j):
        return solve_grid(i, j+1)
    for k in range(1, N+1):
        if check_valid_value(i, j, k):
            grid[i][j] = k
            cpy_grid[i][j] = k
            if solve_grid(i, j+1):
                return True
            grid[i][j] = 0
            cpy_grid[i][j] = 0
    return False

#This function generates cells in the grid
def generate_cells():
    for k in range(0, N, root_N):
        for i in range(root_N):
            for j in range(root_N):
                n = random.randint(1, N)
                while not check_valid_value(k+i, k+j, n) or \
                      check_original_cell(k+i, k+j):
                    n = random.randint(1, N)
                grid[k+i][k+j] = n
                cpy_grid[k+i][k+j] = n

#This function removes cells in the grid
def remove_cells():
    for k in range((N+1)//2):
        for i in range(0, N, root_N):
            for j in range(0, N, root_N):
                t1 = random.randint(0, root_N-1)
                t2 = random.randint(0, root_N-1)
                while not check_original_cell(i+t1, j+t2):
                    t1 = random.randint(0, root_N-1)
                    t2 = random.randint(0, root_N-1)
                grid[i+t1][j+t2] = 0
                cpy_grid[i+t1][j+t2] = 0

#This function generates cells in the given grid
def generate_grid():
    #Generate cells in the grid
    generate_cells()    
    #Solve the complete grid
    solve_grid(0, 0)
    #Remove cells in the grid to be solved
    remove_cells()

#This function clears the game structures
def grid_clear():
    pass

#This function reads a valid position and value inputs
def read_input():
    i, j, v = map(int, input('Enter the row index and column index and value: ').split())
    while not check_valid_position(i, j) or not check_valid_value(i, j, v) or check_original_cell(i, j):
        i, j, v = map(int, input('Enter a valid row index and column index and value: ').split())
    return i, j, v


#MAIN FUNCTION
def play_game():
    print("Sudoku Game!")
    print("Welcome...")
    print("============================")
    while True:
        #Prints the grid
        print_grid()
        #Read an input from the player
        i, j, v = read_input()
        #Set the input position with the value
        set_cell(i, j, v)
        #Check if the grid has a win state
        if check_win():
            #Prints the grid
            print_grid()
            #Announcement of the final statement
            print('Congrats, You won!')
            break

while True:
    grid_clear()
    generate_grid()
    play_game()
    c = input('Play Again [Y/N] ')
    if c not in 'yY':
        break
