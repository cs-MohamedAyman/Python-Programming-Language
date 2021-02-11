import random
N = 4
GOAL = 1 << (3*N-1)
grid = []

#This function prints the grid of 2048 Game as the game progresses
def print_grid():
    print(('-' * N) + ('-' * ((N+4) * N)) + '-')
    for i in range(N):
        print(end='|')
        for j in range(N):
            if grid[i][j] == 0:
                e = ' ' * (N+4)
            else:
                str_len = len(str(grid[i][j]))
                r1 = ((N+4) - str_len + 1) // 2
                r2 = ((N+4) - str_len) - r1
                e = (' ' * r1) + str(grid[i][j]) + (' ' * r2)
            print(e, end='|')
        print()
        print(('-' * N) + ('-' * ((N+4) * N)) + '-')

#This function generates a cell with value 2 
def generate_cell():
    a = random.randint(0, N-1)
    b = random.randint(0, N-1)
    while grid[a][b] != 0:
        a = random.randint(0, N-1)
        b = random.randint(0, N-1)
    grid[a][b] = 2

#This function rotates the grid by 90 degree
def rotate_90():
    for i in range(N//2):
        for j in range(i, N-i-1):
            k                  = grid[i][j]
            grid[i][j]         = grid[N-j-1][i]
            grid[N-j-1][i]     = grid[N-i-1][N-j-1]
            grid[N-i-1][N-j-1] = grid[j][N-i-1]
            grid[j][N-i-1]     = k

#This function checks if the game state reachs 2048 or not 
def check_win():
    pass

#This function checks if the direction have state reachs 2048 or not 
def check_available_direction():
    pass

#This function checks if any direction have state reachs 2048 or not
def check_available_move(d):
    res = False
    #check direction right
    if d == 3: res = check_available_direction()
    rotate_90()
    #check direction down
    if d == 5: res = check_available_direction()
    rotate_90()
    #check direction left
    if d == 1: res = check_available_direction()
    rotate_90()
    #check direction up
    if d == 2: res = check_available_direction()
    rotate_90()
    return res

#This function checks if the game state over or not
def check_full():
    pass

#This function merges the grid with given direction 
def merge():
    pass

#This function checks if the direction have state reachs 2048 or not 
def merge_direction(d):
    #merge direction right
    if d == 3: merge()
    rotate_90()
    #merge direction down
    if d == 5: merge()
    rotate_90()
    #merge direction left
    if d == 1: merge()
    rotate_90()
    #merge direction up
    if d == 2: merge()
    rotate_90()

#This function moves the grid with given direction 
def move():
    pass

#This function checks if the direction have state reachs 2048 or not 
def move_direction(d):
    #move direction left
    if d == 1: move()
    rotate_90()
    #move direction up
    if d == 2: move()
    rotate_90()
    #move direction right
    if d == 3: move()
    rotate_90()
    #move direction down
    if d == 5: move()
    rotate_90()

#This function checks if given position is valid or not 
def check_valid_direction(i):
    pass

#This function clears the grid
def grid_clear():
    pass


#MAIN FUNCTION
def play_game():
    print(str(GOAL) + " Game!")
    print("Welcome...")
    print("============================")
    while True:
        #Generate a cell in the grid
        generate_cell()
        #Prints the grid
        print_grid()
        #Check if the state of the grid has a tie state
        if check_full():
            print("Game Over!")
            break
        #Read an input from the player
        i = int(input('Enter the direction: '))
        while not check_valid_direction(i) or not check_available_move(i):
            i = int(input('Enter a valid direction: '))
        #Move with the input direction
        move_direction(i)
        #Merge with the input direction
        merge_direction(i)
        #Move with the input direction
        move_direction(i)
        #Check if the state of the grid has a win state
        if check_win():
            #Prints the grid
            print_grid()
            print('Congrats, You won!')
            c = input('Continue [Y/N] ')
            if c not in 'yY':
                break

while True:
	grid_clear()
	play_game()
	c = input('Play Again [Y/N] ')
	if c not in 'yY':
		break
