N, M = 15, 15
a_row = 5
n_players = 2
marks = ['X', 'O']
grid = []

#This function prints the grid of Gomoku as the game progresses
def print_grid():
    for i in range(n_players):
        print('Player %d: %c  ' % (i+1, marks[i]), end='')
        if i < n_players-1:
            print('vs  ', end='')
    print()
    print('--' + '---' * M + '--')
    for i in range(N):
        print(end='|  ')
        for j in range(M):
            print(grid[i][j], end='  ')
        print(end='|')
        print()
        print('--' + '---' * M + '--')

#This function checks if the game has a win state or not
def check_win():
    #Check if there is an accepted row
	#the game is over and the player with that character has won
    for i in range(N):
        for j in range(M-a_row+1):
            s = set()
            for k in range(j, j+a_row):
                s |= {grid[i][k]}
            if len(s) == 1 and '.' not in s:
                return True
    #Check if there is an accepted column
    #the game is over and the player with that character has won
    for i in range(M):
        for j in range(N-a_row+1):
            s = set()
            for k in range(j, j+a_row):
                s |= {grid[k][i]}
            if len(s) == 1 and '.' not in s:
                return True
    #Check if there is an accepted left diagonal
    #the game is over and the player with that character has won
    for i in range(N):
        if i+a_row-1 >= N:
            continue
        for j in range(M):
            if j+a_row-1 >= M:
                continue
            s = set()
            for k in range(a_row):
                s |= {grid[i+k][j+k]}
            if len(s) == 1 and '.' not in s:
                return True
    #Check if there is an accepted right diagonal
    #the game is over and the player with that character has won
    for i in range(N):
        if i+a_row-1 >= N:
            continue
        for j in range(M):
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

#This function checks if the game has a tie state or not for the given mark
def check_tie(mark):
    #Check if there is an accpted row
    for i in range(N):
        for j in range(M-a_row+1):
            s = {mark}
            for k in range(j, j+a_row):
                if grid[i][k] != '.':
                    s |= {grid[i][k]}
            if len(s) == 2 and '.' in s:
                return False
    #Check if there is an accpted column
    for i in range(M):
        for j in range(N-a_row+1):
            s = {mark}
            for k in range(j, j+a_row):
                s |= {grid[k][i]}
            if len(s) == 2 and '.' in s:
                return False
    #Check if there is an accpted left diagonal
    for i in range(N):
        if i+a_row-1 >= N:
            continue
        for j in range(M):
            if j+a_row-1 >= M:
                continue
            s = {mark}
            for k in range(a_row):
                s |= {grid[i+k][j+k]}
            if len(s) == 2 and '.' in s:
                return False
    #Check if there is an accpted right diagonal
    for i in range(N):
        if i+a_row-1 >= N:
            continue
        for j in range(M):
            if j-a_row+1 < 0:
                continue
            s = {mark}
            for k in range(a_row):
                s |= {grid[i+k][j-k]}
            if len(s) == 2 and '.' in s:
                return False
    #Otherwise, there isn't a tie state in the game, 
    #if all cases above not reached
    return True

#This function checks if the game has a tie state or not
def check_tie():
    all_tie = True
    for mark in marks:
        if not check_tie(mark):
            all_tie = False
    return all_tie

#This function checks if given cell is empty or not 
def check_empty(i, j):
	return grid[i][j] == '.'

#This function checks if given position is valid or not 
def check_valid_position(i, j):
	return 0 <= i < N and 0 <= j < M

#This function sets the given mark to the given cell
def set_cell(i, j, mark):
	grid[i][j] = mark

#This function clears the game structures
def grid_clear():
	global grid
	grid = [['.'] * M for i in range(N)]

#This function reads a valid position input
def read_input():
    i, j = map(int, input('Enter the row index and column index: ').split())
    while not check_valid_position(i, j) or not check_empty(i, j):
        i, j = map(int, input('Enter a valid row index and a valid column index: ').split())
    return i, j


#MAIN FUNCTION
def play_game():
    print("Gomoku Game!")
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
        player = (player + 1) % n_players


while True:
	grid_clear()
	play_game()
	c = input('Play Again [Y/N] ')
	if c not in 'yY':
		break
