import random
N = 3
grid = []

#This function prints the grid of 8 Puzzle Game as the game progresses
def print_grid():
    print('-' * (N * N + N + 1))
    for i in range(N):
        print(end='|')
        for j in range(N):
            if grid[i][j] == 0:
                e = ' ' * N
            else:
                str_len = len(str(grid[i][j]))
                r1 = (N - str_len + 1) // 2
                r2 = (N - str_len) - r1
                e = (' ' * r1) + str(grid[i][j]) + (' ' * r2)
            print(e, end='|')
        print()
        print('-' * (N * N + N + 1))

#This function generates cells in the given grid
def generate_grid():
    for i in range(1, N*N):
        a = random.randint(0, N-1)
        b = random.randint(0, N-1)
        while grid[a][b] != 0:
            a = random.randint(0, N-1)
            b = random.randint(0, N-1)
        grid[a][b] = i

#This function checks if the game state reachs the win state or not 
def check_win():
    pass

#This function checks if given cell is empty or not 
def check_empty(i, j):
    pass

#This function checks if given position is valid or not 
def check_valid_position(i, j):
    pass

#This function checks if the given position has a movement state or not
def check_available_move(i, j):
    pass

#This function moves the position with the empty cell
def move(i, j):
    pass

#This function clears the game structures
def grid_clear():
    pass

#This function reads a valid position
def read_input():
    i, j = map(int, input('Enter the row index and column index: ').split())
    while not check_valid_position(i, j) or check_empty(i, j) or not check_available_move(i, j):
        i, j = map(int, input('Enter a valid row index and a valid column index: ').split())
    return i, j


#MAIN FUNCTION
def play_game():
    print("8 Puzzle Game!")
    print("Welcome...")
    print("============================")
    while True:
        #Prints the grid
        print_grid()
        #Read an input from the player
        i, j = read_input()
        #Move with the input position
        move(i, j)
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
