N = 7
a_row = 5
grid = []

#This function prints the grid of Gomoku as the game progresses
def print_grid():
    print("Player 1: B  vs  Player 2: W")
    print('--' + '---' * N + '--')
    for i in range(N):
        print(end='|  ')
        for j in range(N):
            print(grid[i][j], end='  ')
        print(end='|')
        print()
        print('--' + '---' * N + '--')

#This function checks if row or column or diagonal is full with same characters
def check_win():
    #If row is full with same characters, 
	#the game is over and the player with that character has won
    for i in range(N):
        for j in range(N-a_row+1):
            s = set()
            for k in range(j, j+a_row):
                s |= {grid[i][k]}
            if len(s) == 1 and '.' not in s:
                return True
    #If column is full with same characters, 
	#the game is over and the player with that character has won
    for i in range(N):
        for j in range(N-a_row+1):
            s = set()
            for k in range(j, j+a_row):
                s |= {grid[k][i]}
            if len(s) == 1 and '.' not in s:
                return True
    #If diagonal is full with same characters, 
	#the game is over and the player with that character has won
    for i in range(N):
        if i+a_row-1 >= N:
            continue
        for j in range(N):
            if j+a_row-1 >= N:
                continue
            s = set()
            for k in range(a_row):
                s |= {grid[i+k][j+k]}
            if len(s) == 1 and '.' not in s:
                return True
    #If diagonal is full with same characters, 
	#the game is over and the player with that character has won
    for i in range(N):
        if i+a_row-1 >= N:
            continue
        for j in range(N):
            if j-a_row+1 < 0:
                continue
            s = set()
            for k in range(a_row):
                s |= {grid[i+k][j-k]}
            if len(s) == 1 and '.' not in s:
                return True
    #Otherwise, there isn't a win state in the game, 
    #if all cases above not reached
    return False

#This function checks if row or column or diagonal is full with same characters
def check_tie(mark):
    #If row a single type of characters
    for i in range(N):
        for j in range(N-a_row+1):
            s = {mark}
            for k in range(j, j+a_row):
                if grid[i][k] != '.':
                    s |= {grid[i][k]}
            if len(s) == 1:
                return False
    #If column a single type of characters
    for i in range(N):
        for j in range(N-a_row+1):
            s = {mark}
            for k in range(j, j+a_row):
                s |= {grid[k][i]}
            if len(s) == 1 and '.' not in s:
                return True
    #If diagonal a single type of characters
    for i in range(N):
        if i+a_row-1 >= N:
            continue
        for j in range(N):
            if j+a_row-1 >= N:
                continue
            s = {mark}
            for k in range(a_row):
                s |= {grid[i+k][j+k]}
            if len(s) == 1 and '.' not in s:
                return True
    #If diagonal a single type of characters
    for i in range(N):
        if i+a_row-1 >= N:
            continue
        for j in range(N):
            if j-a_row+1 < 0:
                continue
            s = {mark}
            for k in range(a_row):
                s |= {grid[i+k][j-k]}
            if len(s) == 1 and '.' not in s:
                return True
    #Otherwise, there isn't a win state in the game, 
    #if all cases above not reached
    return True

#This function checks if given cell is empty or not 
def check_empty(i, j):
	return grid[i][j] == '.'

#This function checks if given position is valid or not 
def check_valid_position(i, j):
	return 0 <= i < N and 0 <= j < N

#This function sets a value to a cell
def set_cell(i, j, mark):
	grid[i][j] = mark

#This function clears the grid
def grid_clear():
	global grid
	grid = [['.'] * N for i in range(N)]


#MAIN FUNCTION
def play_game():
    print("Gomoku Game!")
    print("Welcome...")
    print("============================")
    player = 0
    while True:
        #Prints the grid
        print_grid()
        #Set mark value based on the player
        mark = 'B' if player == 0 else 'W'
        #Read an input from the player
        print('Player %s' % mark)
        i, j = map(int, input('Enter the row index and column index: ').split())
        while not check_valid_position(i, j) or not check_empty(i, j):
            i, j = map(int, input('Enter a valid row index and a valid column index: ').split())
        #Set the input position with the mark
        set_cell(i, j, mark)
        #Check if the state of the grid has a win state
        if check_win():
            #Prints the grid
            print_grid()
            print('Congrats, Player %s is won!' % mark)
            break
        #Check if the state of the grid has a tie state
        if check_tie(mark):
            #Prints the grid
            print_grid()
            print("Woah! That's a tie!")
            break		
        #Player number changes after each turn
        player = 1 - player 


while True:
	grid_clear()
	play_game()
	c = input('Play Again [Y/N] ')
	if c not in 'yY':
		break
