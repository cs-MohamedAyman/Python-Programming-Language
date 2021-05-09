import random
N, M = 4, 4
viewed_grid, grid = [], []

#This function prints the grid of Match Cards Game as the game progresses
def print_grid():
    print('-' * (4 * M + M + 1))
    for i in range(N):
        print(end='|')
        for j in range(M):
            if viewed_grid[i][j] == 0:
                e = '    '
            else:
                e = str(grid[i][j])
                if len(e) == 1: e = ' ' + e
                e = ' ' + e + ' '
            print(e, end='|')
        print()
        print('-' * (4 * M + M + 1))

#This function checks if the game state reachs the win state or not 
def check_win():
    pass

#This function generates cells in the given grid
def generate_grid():
    for i in range(1, N*M//2+1):
        for j in range(2):
            a = random.randint(0, N-1)
            b = random.randint(0, M-1)
            while grid[a][b] != 0:
                a = random.randint(0, N-1)
                b = random.randint(0, M-1)
            grid[a][b] = i

#This function checks if given position is valid or not 
def check_valid_position(i, j):
    pass

#This function checks if the given cells are identical cells or not
def check_identical_cells(i1, j1, i2, j2):
    pass

#This function shows the given cell
def show(i, j):
    pass

#This function hides the given cell
def hide(i, j):
    pass

#This function checks if the given position is hidden or not
def check_hide_cell(i, j):
    pass

#This function checks if the given positions are the same or not
def check_same_position(i1, j1, i2, j2):
    pass

#This function clears the game structures
def grid_clear():
    pass

#This function reads a valid input of cells
def read_input():
    i1, j1, i2, j2 = map(int, input('Enter the two positions of the cells: ').split())
    while not check_valid_position(i1, j1) or not check_valid_position(i2, j2) or \
          not check_hide_cell(i1, j1) or not check_hide_cell(i2, j2) or check_same_position(i1, j1, i2, j2):
        i1, j1, i2, j2 = map(int, input('Enter a valid two positions of the cells: ').split())
    return i1, j1, i2, j2


#MAIN FUNCTION
def play_game():
    print("Match Cards Game!")
    print("Welcome...")
    print("============================")
    while True:
        #Prints the grid
        print_grid()
        #Read an input from the player
        i1, j1, i2, j2 = read_input()
        #Show the input cells
        show(i1, j1)
        show(i2, j2)
        #Prints the grid
        print_grid()
        #Check if the input cells are identical
        if not check_identical_cells(i1, j1, i2, j2):
            #Hide the input cells
            hide(i1, j1)
            hide(i2, j2)
            print('The selected cells are not the same')
        else:
            print('The selected cells are the same')
        #Check if the grid has a win state
        if check_win():
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
