'''
Assigning values to the grid
The grid will look like this:
  0,0 | 0,1 | 0,2 | 0,3 
  1,0 | 1,1 | 1,2 | 1,3 
  2,0 | 2,1 | 2,2 | 2,3 
  3,0 | 3,1 | 3,2 | 3,3 
'''
import random
N = 4
grid = [[0] * N for i in range(N)]

#This function prints the grid of 2048 Game as the game progresses
def print_grid():
    print('--' + '-----' * N + '----')
    for i in range(N):
        print(end='|  ')
        for j in range(N):
            r = (5 - len(str(grid[i][j]))) // 2
            e = (' ' * r) + str(grid[i][j]) + (' ' * r)
            if len(e) < 5: e += ' '
            print(e, end='')
        print(end='  |')
        print()
        print('--' + '-----' * N + '----')

#This function generates a cell with value 2 
def generate_cell():
    a = random.randint(0, N-1)
    b = random.randint(0, N-1)
    while grid[a][b] != 0:
        a = random.randint(0, N-1)
        b = random.randint(0, N-1)
    grid[a][b] = 2

#This function checks if the game state reachs 2048 or not 
def check_win():
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 2048:
                return True
    return False

#This function rotates the grid by 90 degree
def rotate_90():
    for i in range(N//2):
        for j in range(i, N-i-1):
            k                  = grid[i][j]
            grid[i][j]         = grid[N-j-1][i];
            grid[N-j-1][i]     = grid[N-i-1][N-j-1];
            grid[N-i-1][N-j-1] = grid[j][N-i-1]
            grid[j][N-i-1]     = k

#This function checks if the direction have state reachs 2048 or not 
def check_available_direction():
    for i in range(N):
        j = 0
        while j < N and grid[i][j] == 0: j +=1 
        while j < N and grid[i][j] != 0: j +=1 
        if j < N: return True
        for k in range(N-1):
            if grid[i][k] == grid[i][k+1] and grid[i][k] != 0:
                return True
    return False

#This function checks if any direction have state reachs 2048 or not
def check_available_move(dir):
    res = False
    #check direction right
    if dir == 3: res = check_available_direction()
    rotate_90()
    #check direction down
    if dir == 5: res = check_available_direction()
    rotate_90()
    #check direction left
    if dir == 1: res = check_available_direction()
    rotate_90()
    #check direction up
    if dir == 2: res = check_available_direction()
    rotate_90()
    return res

#This function checks if the game state over or not
def check_full():
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                return False
    for i in range(N-1):
        if grid[N-1][i] == grid[N-1][i+1]:
            return False
    for i in range(N-1):
        if grid[i][N-1] == grid[i+1][N-1]:
            return False
    for i in range(N-1):
        for j in range(N-1):
            if grid[i][j] == grid[i+1][j] or grid[i][j+1] == grid[i][j]:
                return False
    return True

#This function merges the grid with given direction 
def merge():
    for i in range(N):
        j = N-1
        while j > 0:
            if grid[i][j] == grid[i][j-1] and grid[i][j] != 0:
                grid[i][j] = 0
                grid[i][j-1] *= 2
                j -= 1
            j -= 1

#This function checks if the direction have state reachs 2048 or not 
def merge_direction(dir):
    #merge direction right
    if dir == 3: merge()
    rotate_90()
    #merge direction down
    if dir == 5: merge()
    rotate_90()
    #merge direction left
    if dir == 1: merge()
    rotate_90()
    #merge direction up
    if dir == 2: merge()
    rotate_90()

#This function moves the grid with given direction 
def move():
    for i in range(N):
        temp = []
        for j in range(N):
            if grid[i][j] != 0:
                temp += [grid[i][j]]
        for j in range(N):
            grid[i][j] = temp[j] if j < len(temp) else 0

#This function checks if the direction have state reachs 2048 or not 
def move_direction(dir):
    #move direction left
    if dir == 1: move()
    rotate_90()
    #move direction up
    if dir == 2: move()
    rotate_90()
    #move direction right
    if dir == 3: move()
    rotate_90()
    #move direction down
    if dir == 5: move()
    rotate_90()

#This function checks if given position is valid or not 
def check_valid_direction(i):
	return i in [1, 2, 3, 5]

#This function clears the grid
def grid_clear():
	global grid
	grid = [[0] * N for i in range(N)]


#MAIN FUNCTION
def play_game():
    print("2048 Game!")
    print("Welcome...")
    print("============================")
    while True:
        #Generate a cell in the grid
        generate_cell()
        #Prints the grid
        print_grid()
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
            break
        #Check if the state of the grid has a tie state
        if check_full():
            #Prints the grid
            print_grid()
            print("Woah! That's a tie!")
            break

while True:
	play_game()
	grid_clear()
	c = input('Play Again [Y/N] ')
	if c not in 'yY':
		break
