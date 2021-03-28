N = 3
n_players = 2
marks = ['X', 'O']
grid = []

#This function prints the grid of Tic-Tac-Toe Game as the game progresses
def print_grid():
    print("Player 1: %c  vs  Player 2: %c" % (marks[0], marks[1]))
    print('--' + '---' * N + '--')
    for i in range(N):
        print(end='|  ')
        for j in range(N):
            print(grid[i][j], end='  ')
        print(end='|')
        print()
        print('--' + '---' * N + '--')

#This function checks if the game has a win state or not
def check_win():
    #Check if there is a row with full with same characters, 
	#the game is over and the player with that character has won
	for i in range(N):
		s = set()
		for j in range(N):
			s |= {grid[i][j]}
		if len(s) == 1 and '.' not in s:
			return True
    #Check if there is a column with full with same characters, 
	#the game is over and the player with that character has won
	for i in range(N):
		s = set()
		for j in range(N):
			s |= {grid[j][i]}
		if len(s) == 1 and '.' not in s:
			return True
    #Check if the left diagonal is full with same characters, 
	#the game is over and the player with that character has won
	s = set()
	for i in range(N):
		s |= {grid[i][i]}
	if len(s) == 1 and '.' not in s:
		return True
    #Check if the right diagonal is full with same characters, 
	#the game is over and the player with that character has won
	s = set()
	for i in range(N):
		s |= {grid[i][N-i-1]}
	if len(s) == 1 and '.' not in s:
		return True
    #Otherwise, there isn't a win state in the game, 
    #if all cases above not reached
	return False

#This function checks if the game has a tie state or not for the given mark
def check_tie_player(mark):
    #Check if there is a row with a single type of characters
	for i in range(N):
		s = {mark}
		for j in range(N):
			if grid[i][j] != '.':
				s |= {grid[i][j]}
		if len(s) == 1:
			return False
    #Check if there is a column with a single type of characters
	for i in range(N):
		s = {mark}
		for j in range(N):
			if grid[j][i] != '.':
				s |= {grid[j][i]}
		if len(s) == 1:
			return False
    #Check if the left diagonal is a single type of characters
	s = {mark}
	for i in range(N):
		if grid[i][i] != '.':
			s |= {grid[i][i]}
	if len(s) == 1:
			return False
    #Check if the right diagonal is a single type of characters
	s = {mark}
	for i in range(N):
		if grid[i][N-i-1] != '.':
			s |= {grid[i][N-i-1]}
	if len(s) == 1:
		return False
    #Otherwise, there isn't a win state in the game, 
    #if all cases above not reached
	return True

#This function checks if the game has a tie state or not
def check_tie():
    all_tie = True
    for i in range(n_players):
        if not check_tie_player(marks[i]):
            all_tie = False
    return all_tie

#This function checks if given cell is empty or not 
def check_empty(i, j):
	return grid[i][j] == '.'

#This function checks if given position is valid or not 
def check_valid_position(i, j):
	return 0 <= i < N and 0 <= j < N

#This function sets the given mark to the given cell
def set_cell(i, j, mark):
	grid[i][j] = mark

#This function clears the game structures
def grid_clear():
	global grid
	grid = [['.'] * N for i in range(N)]

#This function reads a valid position input
def read_input():
    i, j = map(int, input('Enter the row index and column index: ').split())
    while not check_valid_position(i, j) or not check_empty(i, j):
        i, j = map(int, input('Enter a valid row index and a valid column index: ').split())
    return i, j


#MAIN FUNCTION
def play_game():
    print("Tic-Tac-Toe Game!")
    print("Welcome...")
    print("============================")
    player = 0
    while True:
        #Prints the grid
        print_grid()
        #Read an input position from the player
        print('Player %s is playing now' % marks[player])
        i, j = read_input()
        #Set the player mark in the input position
        set_cell(i, j, marks[player])
        #Check if the grid has a win state
        if check_win():
            #Prints the grid
            print_grid()
            #Announcement of the final statement
            print('Congrats, Player %s is won!' % marks[player])
            break
        #Check if the grid has a tie state
        if check_tie():
            #Prints the grid
            print_grid()
            #Announcement of the final statement
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
