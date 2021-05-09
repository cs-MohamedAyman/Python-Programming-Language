import random
N, M = 8, 8
mines = 8
viewed_grid, grid = [], []

#This function prints the grid of Minesweeper Game as the game progresses
def print_grid():
    print('-' * (5 * M + M + 1))
    for i in range(N):
        print(end='|')
        for j in range(M):
            if viewed_grid[i][j] == 0:
                e = '  .  '
            elif viewed_grid[i][j] == 2:
                e = '  F  '
            elif grid[i][j] == 0:
                e = '     '
            elif grid[i][j] == -1:
                e = '  *  '
            else:
                e = '  ' + str(grid[i][j]) + '  '
            print(e, end='|')
        print()
        print('-' * (5 * M + M + 1))
    
#This function generates mines in the grid
def generate_mines():
    for i in range(mines):
        a = random.randint(0, N-1)
        b = random.randint(0, M-1)
        while grid[a][b] != 0:
            a = random.randint(0, N-1)
            b = random.randint(0, M-1)
        grid[a][b] = -1

#This function checks if given position is valid or not 
def check_valid_position(i, j):
    pass

#This function calculates the total number of mines in the neighbour cells
def calc_neighbour_mines():
    pass
            
#This function generates cells in the grid
def generate_grid():
    #Generate mines in the grid
    generate_mines()
    #Calculate neighbour mines in the grid
    calc_neighbour_mines()

#This function checks if the given position is hidden or not
def check_hide_cell(i, j):
    pass

#This function checks if the given position is viewed or not
def check_mines_cell(i, j):
    pass

#This function checks if the given position is viewed or not
def check_view_cell(i, j):
    pass

#This function checks if the given position is flagged or not
def check_flag_cell(i, j):
    pass

#This function checks if the game state reachs the win state or not 
def check_win():
    pass

#This function checks if given operation is valid or not 
def check_valid_operation(x):
    pass

#This function flips the flag mark to the given cell
def flip_flag(i, j):
    pass

#This function showes the given cell
def show_cell(i, j):
    pass

#This function showes all mines cells
def show_all_mines():
    pass

#This function clears the game structures
def grid_clear():
    pass

#This function reads a valid position
def read_input():
    i, j, op = input('Enter the position and operation type: ').split()
    i, j = int(i), int(j)
    while not check_valid_position(i, j) or check_view_cell(i, j) or not check_valid_operation(op) or \
          (op.lower() == 'f' and check_view_cell(i, j)) or (op.lower() == 's' and not check_hide_cell(i, j)):
        i, j, op = input('Enter a valid position and a valid operation type: ').split()
        i, j = int(i), int(j)
    return i, j, op.lower()


#MAIN FUNCTION
def play_game():
    print("Minesweeper Game!")
    print("Welcome...")
    print("============================")
    while True:
        #Prints the grid
        print_grid()
        #Read an input from the player
        i, j, op = read_input()
        #Flip the cell with a flag
        if op == 'f':
            flip_flag(i, j)
        #Show the cell
        else:
            show_cell(i, j)
            #Check if the grid has a mines state
            if check_mines_cell(i, j):
                #Show the cell
                show_all_mines()
                #Prints the grid
                print_grid()
                #Announcement of the final statement
                print('Game Over!')
                break
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
