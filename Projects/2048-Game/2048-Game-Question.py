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
    pass

#This function checks if the game state reachs 2048 or not 
def check_win():
    pass

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
    pass

#This function checks if any direction have state reachs 2048 or not
def check_available_move(dir):
    pass

#This function checks if the game state over or not
def check_full():
    pass

#This function merges the grid with given direction 
def merge():
    pass

#This function checks if the direction have state reachs 2048 or not 
def merge_direction(dir):
    pass

#This function moves the grid with given direction 
def move():
    pass

#This function checks if the direction have state reachs 2048 or not 
def move_direction(dir):
    pass

#This function checks if given position is valid or not 
def check_valid_direction(i):
    pass

#This function clears the grid
def grid_clear():
    pass


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
