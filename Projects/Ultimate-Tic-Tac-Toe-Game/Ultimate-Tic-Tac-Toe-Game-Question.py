N = 3
marks = ['X', 'O']
small_grid, big_grid = [], []
curr_box, next_box = -1, -1

#This function prints the grid of Tic-Tac-Toe Game as the game progresses
def print_grid():
    print("Player 1: %c  vs  Player 2: %c" % (marks[0], marks[1]))
    print(('-' * (N*N*3)) + ('---' * N) + '-')
    for i in range(N*N):
        print(end='|  ')
        for j in range(N*N):
            if j % N == 0 and j > 0:
                print('|  ', end='')
            print(big_grid[i][j], end='  ')
        print(end='|')
        print()
        if i % N == N - 1:
            print(('-' * (N*N*3)) + ('---' * N) + '-')

#This function converts the given position in the big grid into a box number
def cvt_big_grid_pos_to_box(i, j):
    return i // N * N + j // N

#This function converts the given box number into a position index in the big grid
def cvt_box_to_big_grid_pos(x):
    return x // N * N, x % N * N

#This function converts the given position in the small grid into a box number
def cvt_small_grid_pos_to_box(i, j):
    return i * N + j

#This function converts the given box number into a position index in the small grid
def cvt_box_to_small_grid_pos(x):
    return x // N, x % N

#This function converts the given position in the big grid into a position index in the big grid
def cvt_big_grid_pos_to_big_grid_pos(i, j):
	box_idx = cvt_big_grid_pos_to_box(i, j)
	i, j = cvt_box_to_big_grid_pos(box_idx)
	return i, j

#This function converts the given position in the big grid into a position index in the small grid
def cvt_big_grid_pos_to_small_grid_pos(i, j):
	box_idx = cvt_big_grid_pos_to_box(i, j)
	i, j = cvt_box_to_small_grid_pos(box_idx)
	return i, j

#This function checks if the game has a win state or not
def check_win(grid, r=0, c=0):
    #Convert the given position in the big grid into a position index in the big grid
    r, c = cvt_big_grid_pos_to_big_grid_pos(r, c)
    #Check if there is a row with full with same characters, 
    #the game is over and the player with that character has won
    for i in range(r, r+N):
        s = set()
        for j in range(c, c+N):
            s |= {grid[i][j]}
        if len(s) == 1 and '.' not in s:
            return True
    #Check if there is a column with full with same characters, 
    #the game is over and the player with that character has won
    for i in range(c, c+N):
        s = set()
        for j in range(r, r+N):
            s |= {grid[j][i]}
        if len(s) == 1 and '.' not in s:
            return True
    #Check if the left diagonal is full with same characters, 
    #the game is over and the player with that character has won
    s = set()
    for i in range(N):
        s |= {grid[r+i][c+i]}
    if len(s) == 1 and '.' not in s:
        return True
    #Check if the right diagonal is full with same characters, 
    #the game is over and the player with that character has won
    s = set()
    for i in range(N):
        s |= {grid[r+i][c+N-i-1]}
    if len(s) == 1 and '.' not in s:
        return True
    #Otherwise, there isn't a win state in the game, 
    #if all cases above not reached
    return False

#This function checks if the game has a tie state or not
def check_tie(grid, mark, r=0, c=0):
	#Convert the given position in the big grid into a position index in the big grid
	r, c = cvt_big_grid_pos_to_big_grid_pos(r, c)
	#Check if there is a row with a single type of characters
	for i in range(r, r+N):
		s = {mark}
		for j in range(c, c+N):
			if grid[i][j] != '.':
				s |= {grid[i][j]}
		if len(s) == 1:
			return False
    #Check if there is a column with a single type of characters
	for i in range(c, c+N):
		s = {mark}
		for j in range(r, r+N):
			if grid[j][i] != '.':
				s |= {grid[j][i]}
		if len(s) == 1:
			return False
    #Check if the left diagonal is a single type of characters
	s = {mark}
	for i in range(N):
		if grid[r+i][c+i] != '.':
			s |= {grid[r+i][c+i]}
	if len(s) == 1:
			return False
    #Check if the right diagonal is a single type of characters
	s = {mark}
	for i in range(N):
		if grid[r+i][c+N-i-1] != '.':
			s |= {grid[r+i][c+N-i-1]}
	if len(s) == 1:
		return False
    #Otherwise, there isn't a win state in the game, 
    #if all cases above not reached
	return True

#This function checks if the given cell in the big grid is empty or not 
def check_empty_in_big_grid(i, j):
	return big_grid[i][j] == '.'

#This function checks if the given cell in the small grid is empty or not 
def check_empty_in_small_grid(i, j):
    return small_grid[i][j] == '.'

#This function checks if given position is valid or not 
def check_valid_position(i, j):
	return 0 <= i < N*N and 0 <= j < N*N

#This function calculates the current selected box 
def set_next_box(i, j):
    global next_box
    x, y = cvt_big_grid_pos_to_big_grid_pos(i, j)
    si, sj = i - x, j - y
    next_box = cvt_small_grid_pos_to_box(si, sj)
    if not check_empty_in_small_grid(si, sj):
        next_box = -1

#This function sets the given mark to the given cell in the big grid
def set_cell_in_big_grid(i, j, mark):
    global curr_box
    big_grid[i][j] = mark
    curr_box = cvt_big_grid_pos_to_box(i, j)

#This function sets the given mark to the given box
def fill_box(r, c, mark):
    r, c = cvt_big_grid_pos_to_small_grid_pos(r, c)
    for i in range(r*N, r*N+N):
        for j in range(c*N, c*N+N):
            big_grid[i][j] = mark
    small_grid[r][c] = mark

#This function clears the game structures
def grid_clear():
    global small_grid, big_grid, curr_box, next_box
    small_grid = [['.'] * N for i in range(N)]
    big_grid   = [['.'] * (N*N) for i in range(N*N)]
    curr_box, next_box = -1, -1

#This function reads a valid position input
def read_input():
    box_idx = 'any box' if next_box == -1 else 'box ' + str(next_box)
    i, j = map(int, input('Enter the row index and column index in %s: ' % box_idx).split())
    si, sj = cvt_big_grid_pos_to_small_grid_pos(i, j)
    while not check_valid_position(i, j) or not check_empty_in_big_grid(i, j) or \
          (next_box != -1 and next_box != cvt_big_grid_pos_to_box(i, j)) or \
          (next_box == -1 and not cvt_big_grid_pos_to_small_grid_pos(si, sj)):
        i, j = map(int, input('Enter a valid row index and column index in %s: ' % box_idx).split())
        si, sj = cvt_big_grid_pos_to_small_grid_pos(i, j)
    return i, j


#MAIN FUNCTION
def play_game():
    print("Ultimate Tic-Tac-Toe Game!")
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
        set_cell_in_big_grid(i, j, marks[player])
        #Check if the selected box has a win state
        if check_win(big_grid, i, j):
            #Prints the grid
            print_grid()
            #Announcement of the final statement in a box
            print('Congrats, Player %s is completed the box %s !' % (marks[player], curr_box))
            fill_box(i, j, marks[player])
        #Check if the selected box has a full state
        elif check_tie(big_grid, marks[player], i, j) and check_tie(big_grid, marks[1-player], i, j):
            #Prints the grid
            print_grid()
            #Announcement of the final statement in a box
            print("Woah! That's a tie in the box %s !" % curr_box)
            fill_box(i, j, '#')
        #Calculate the next selected box 
        set_next_box(i, j)
        #Check if the small grid has a win state
        if check_win(small_grid):
            #Prints the grid
            print_grid()
            #Announcement of the final statement
            print('Congrats, Player %s is won!' % marks[player])
            break
        #Check if the grid has a tie state
        if check_tie(small_grid, marks[player]) and check_tie(small_grid, marks[1-player]):
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
