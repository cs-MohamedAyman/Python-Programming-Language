'''
Assigning values to the grid
The grid will look like this:
  0,0 | 0,1 | 0,2
  1,0 | 1,1 | 1,2
  2,0 | 2,1 | 2,2
'''
N = 3
grid = [['.'] * N for i in range(N)]

#This function prints the grid of Tic-Tac-Toe as the game progresses
def print_grid():
    print("Player 1: X  vs  Player 2: O")
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
		s = set()
		for j in range(N):
			s |= {grid[i][j]}
		if len(s) == 1 and '.' not in s:
			return True
    #If column is full with same characters, 
	#the game is over and the player with that character has won
	for i in range(N):
		s = set()
		for j in range(N):
			s |= {grid[j][i]}
		if len(s) == 1 and '.' not in s:
			return True
    #If diagonal is full with same characters, 
	#the game is over and the player with that character has won
	s = set()
	for i in range(N):
		s |= {grid[i][i]}
	if len(s) == 1 and '.' not in s:
		return True
    #If diagonal is full with same characters, 
	#the game is over and the player with that character has won
	s = set()
	for i in range(N):
		s |= {grid[i][N-i-1]}
	if len(s) == 1 and '.' not in s:
		return True
	return False

#This function checks if row or column or diagonal is full with same characters
def check_tie(mark):
    #If row a single type of characters
	for i in range(N):
		s = {mark}
		for j in range(N):
			if grid[i][j] != '.':
				s |= {grid[i][j]}
		if len(s) == 1:
			return False
    #If column a single type of characters
	for i in range(N):
		s = {mark}
		for j in range(N):
			if grid[j][i] != '.':
				s |= {grid[j][i]}
		if len(s) == 1:
			return False
    #If diagonal a single type of characters
	s = {mark}
	for i in range(N):
		if grid[i][i] != '.':
			s |= {grid[i][i]}
	if len(s) == 1:
			return False
    #If diagonal a single type of characters
	s = {mark}
	for i in range(N):
		if grid[i][N-i-1] != '.':
			s |= {grid[i][N-i-1]}
	if len(s) == 1:
		return False
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
    print("Tic-Tac-Toe Game!")
    print("Welcome...")
    print("============================")
    player = 0
    while True:
        #Prints the grid
        print_grid()
        #Set mark value based on the player
        mark = 'X' if player == 0 else 'O'
        #Takes input from the user to fill in the grid
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
	play_game()
	grid_clear()
	c = input('Play Again [Y/N] ')
	if c not in 'yY':
		break
