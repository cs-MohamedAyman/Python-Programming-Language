'''
Assigning values to the grid
The grid will look like this:
  0,0 | 0,1 | 0,2 | 0,3 | 0,4 | 0,5 | 0,6 | 0,7 | 0,8
  1,0 | 1,1 | 1,2 | 1,3 | 1,4 | 1,5 | 1,6 | 1,7 | 1,8
  2,0 | 2,1 | 2,2 | 2,3 | 2,4 | 2,5 | 2,6 | 2,7 | 2,8
  3,0 | 3,1 | 3,2 | 3,3 | 3,4 | 3,5 | 3,6 | 3,7 | 3,8
  4,0 | 4,1 | 4,2 | 4,3 | 4,4 | 4,5 | 4,6 | 4,7 | 4,8
  5,0 | 5,1 | 5,2 | 5,3 | 5,4 | 5,5 | 5,6 | 5,7 | 5,8
  6,0 | 6,1 | 6,2 | 6,3 | 6,4 | 6,5 | 6,6 | 6,7 | 6,8
  7,0 | 7,1 | 7,2 | 7,3 | 7,4 | 7,5 | 7,6 | 7,7 | 7,8
  8,0 | 8,1 | 8,2 | 8,3 | 8,4 | 8,5 | 8,6 | 8,7 | 8,8
'''
import random
N = 9
grid = [[0] * N for i in range(N)]

#This function prints the grid of 2048 Game as the game progresses
def print_grid():
    print('-' + '----' * N)
    for i in range(N):
        print(end='|  ')
        for j in range(N):
            if j % 3 == 0 and j > 0:
                print('|  ', end='')
            print(grid[i][j], end='  ')
        print(end='|')
        print()
        if i % 3 == 2:
            print('-' + '----' * N)

#This function checks if all rows and columns and boxes is full with all numbers
def check_win():
    for i in range(N):
        s = set()
        for j in range(N):
            s.add(grid[i][j])
        if len(s) != N or 0 in s:
            return False
    for i in range(N):
        s = set()
        for j in range(N):
            s.add(grid[j][i])
        if len(s) != N or 0 in s:
            return False
    for i in range(0, N, 3):
        for j in range(0, N, 3):
            s = set()
            for k in range(i, i+3):
                for w in range(j, j+3):
                    s.add(grid[k][w])
            if len(s) != N*N or 0 in s:
                return False
    return True

#This function checks if given position is valid or not 
def check_valid_position(i, j):
    return 0 <= i < N and 0 <= j < N

#This function checks if given cell is empty or not 
def check_empty_cell(i, j):
    return grid[i][j] == 0

#This function checks if the given cell is valid with the given numbers
def check_valid_value(i, j, v):
    if v == 0:
        return True
    for k in range(N):
        if grid[i][k] == v:
            return False
    for k in range(N):
        if grid[k][j] == v:
            return False
    b, e = i//3*3, j//3*3
    for k in range(b, b+3):
        for w in range(e, e+3):
            if grid[k][w] == v:
                return False
    return True

#This function sets a value to a cell
def set_cell(i, j, v):
	grid[i][j] = v

#This function generates cells in the grid
def generate_cells():
    vals = []
    for i in range(1, N+1):
        vals += [i] * (N//3)
    for i in range(0, N, 3):
        for j in range(0, N, 3):
            for w in range(3):
                random.shuffle(vals)
                k = random.choice(vals)
                while not check_valid_value(i+w, j+w, k):
                    k = random.choice(vals)
                set_cell(i+w, j+w, k)
                vals.remove(k)

#This function clears the grid
def grid_clear():
	global grid
	grid = [[0] * N for i in range(N)]


#MAIN FUNCTION
def play_game():
    print("Sudoku Game!")
    print("Welcome...")
    print("============================")
    while True:
        #Prints the grid
        print_grid()
        i, j, v = map(int, input('Enter the position and value: ').split())
        while not check_valid_position(i, j) or not check_valid_value(i, j, v):
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
    generate_cells()
    play_game()
    grid_clear()
    c = input('Play Again [Y/N] ')
    if c not in 'yY':
        break
