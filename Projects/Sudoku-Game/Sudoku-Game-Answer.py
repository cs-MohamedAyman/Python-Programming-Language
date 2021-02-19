import random
N = 9
root_N = int(N ** 0.5)
grid, cpy_grid = [], []

#This function prints the grid of 2048 Game as the game progresses
def print_grid():
    dd_len = len(str(N))
    print(('-' * (N*(dd_len+2))) + ('---' * root_N) + '-')
    for i in range(N):
        print(end='|  ')
        for j in range(N):
            if j % root_N == 0 and j > 0:
                print('|  ', end='')
            if grid[i][j] == 0:
                print('.'*dd_len, end='  ')
            else:
                print('0'*(dd_len - len(str(grid[i][j]))) + str(grid[i][j]), end='  ')
        print(end='|')
        print()
        if i % root_N == root_N - 1:
            print(('-' * (N*(dd_len+2))) + ('---' * root_N) + '-')

#This function checks if all rows and columns and boxes is full with all numbers
def check_win():
    #If row is not full with all numbers, the game is still running
    for i in range(N):
        s = set()
        for j in range(N):
            s.add(grid[i][j])
        if len(s) != N or 0 in s:
            return False
    #If column is not full with all numbers, the game is still running
    for i in range(N):
        s = set()
        for j in range(N):
            s.add(grid[j][i])
        if len(s) != N or 0 in s:
            return False
    #If box is not full with all numbers, the game is still running
    for i in range(0, N, root_N):
        for j in range(0, N, root_N):
            s = set()
            for k in range(i, i+root_N):
                for w in range(j, j+root_N):
                    s.add(grid[k][w])
            if len(s) != N or 0 in s:
                return False
    #Otherwise, there is a win state in the game, 
    #if all cases above not reached		
    return True

#This function checks if given position is valid or not 
def check_valid_position(i, j):
    return 0 <= i < N and 0 <= j < N

#This function checks if given cell is empty or not 
def check_empty_cell(i, j):
    return grid[i][j] == 0

#This function checks if given cell is original or not
def check_original_cell(i, j):
    return cpy_grid[i][j] != 0

#This function checks if the given cell is valid with the given numbers
def check_valid_value(i, j, v):
	#Check delete case
    if v == 0:
        return True
	#Check invalid value
    if v < 0 or v > N:
        return False
	#Check duplicate in all rows
    for k in range(N):
        if grid[i][k] == v:
            return False
	#Check duplicate in all columns
    for k in range(N):
        if grid[k][j] == v:
            return False
	#Check duplicate in all boxes
    b, e = i//root_N*root_N, j//root_N*root_N
    for k in range(b, b+root_N):
        for w in range(e, e+root_N):
            if grid[k][w] == v:
                return False
    #Otherwise, the given value is valid,
    #if all cases above not reached		
    return True

#This function sets a value to a cell
def set_cell(i, j, v):
	grid[i][j] = v

#This function solve the grid
def solve_grid(i, j):
    if j == N:
        i += 1
        j = 0
    if i == N:
        return True
    if check_original_cell(i, j):
        return solve_grid(i, j + 1)
    for k in range(1, N+1):
        if check_valid_value(i, j, k):
            grid[i][j] = k
            cpy_grid[i][j] = k
            if solve_grid(i, j + 1):
                return True
        grid[i][j] = 0
        cpy_grid[i][j] = 0
    return False

#This function generates cells in the grid
def generate_cells():
    #Generate cells in the diagonal boxes of the grid
    for k in range(0, N, root_N):
        for i in range(root_N):
            for j in range(root_N):
                n = random.randint(1, N)
                while not check_valid_value(k+i, k+j, n) or check_original_cell(k+i, k+j):
                    n = random.randint(1, N)
                grid[k+i][k+j] = n
                cpy_grid[k+i][k+j] = n
    #Solve the complete grid
    solve_grid(0, 0)
    #Remove cells in the grid to be solved
    prev_x, prev_y = 0, 0
    for k in range(N*N - N//2*N):
        i = (random.randint(0, N-1) + prev_x + root_N) % N
        j = (random.randint(0, N-1) + prev_y + root_N) % N
        while not check_original_cell(i, j):
            i = (random.randint(0, N-1) + prev_x + root_N) % N
            j = (random.randint(0, N-1) + prev_y + root_N) % N
        grid[i][j] = 0
        cpy_grid[i][j] = 0
        prev_x, prev_y = i, j

#This function clears the grid
def grid_clear():
	global grid, cpy_grid
	grid = [[0] * N for i in range(N)]
	cpy_grid = [[0] * N for i in range(N)]


#MAIN FUNCTION
def play_game():
    print("Sudoku Game!")
    print("Welcome...")
    print("============================")
    while True:
        #Prints the grid
        print_grid()
        #Read an input from the player
        i, j, v = map(int, input('Enter the position and value: ').split())
        while not check_valid_position(i, j) or not check_valid_value(i, j, v) or check_original_cell(i, j):
            i, j, v = map(int, input('Enter a valid position and value: ').split())
        #Set the input position with the value
        set_cell(i, j, v)
        #Check if the state of the grid has a win state
        if check_win():
            #Prints the grid
            print_grid()
            print('Congrats, You won!')
            break

while True:
    grid_clear()
    generate_cells()
    play_game()
    c = input('Play Again [Y/N] ')
    if c not in 'yY':
        break
