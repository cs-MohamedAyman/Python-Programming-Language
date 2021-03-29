N, M = 8, 8
n_players = 2
marks = ['X', 'O']
count_cells, grid, possible_cells = [], [], []

#This function prints the grid of Reversi as the game progresses
def print_grid():
    print("Player 1: %c  vs  Player 2: %c" % (marks[0], marks[1]))
    print('--' + '---' * M + '--')
    for i in range(N):
        print(end='|  ')
        for j in range(M):
            print(grid[i][j], end='  ')
        print(end='|')
        print()
        print('--' + '---' * M + '--')
    for i in range(n_players):
        print('Player %c has %d cells'% (marks[i], count_cells[i]))
    print('--' + '------' * (M-1))

#This function checks if the game has a full state or not
def check_full():
    for i in range(N):
        for j in range(M):
            if grid[i][j] == '.':
                return False
    return True

#This function checks if the game has a tie state or not
def check_player_ability():
    return len(possible_cells) != 0

#This function checks if given cell is chosen or not 
def check_chosen(i, j):
    return (i, j) in possible_cells

#This function checks if given cell is empty or not 
def check_empty(i, j):
	return grid[i][j] == '.'

#This function checks if given position is valid or not 
def check_valid_position(i, j):
	return 0 <= i < N and 0 <= j < M

#This function calculates the total number of cells for each player
def calc_cells():
    global count_cells
    count_cells = [0] * n_players
    for p in range(n_players):
        for i in range(N):
            for j in range(M):
                if grid[i][j] == marks[p]:
                    count_cells[p] += 1

#This function sets the given mark to the given cell
def set_cell(i, j, mark):
	grid[i][j] = mark

#This function gets the most cell in the given direction
def get_most_cell(i, j, dx, dy, player, target_mark):
    cnt = 0
    while check_valid_position(i, j) and grid[i][j] == marks[1-player]:
        i += dx 
        j += dy
        cnt += 1
    return (i, j) if check_valid_position(i, j) and grid[i][j] == target_mark and cnt > 0 else (-1, -1)

#This function gets the most cells in the all directions
def get_most_cells(i, j, player, target_mark):
    most_cells = []
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for dx, dy in dirs:
        most_i, most_j = get_most_cell(i+dx, j+dy, dx, dy, player, target_mark)
        if most_i == -1 and most_j == -1:
            continue
        most_cells += [(most_i, most_j)]
    return most_cells

#This function switches the neighbor cells of the given cell
def switch_cells(i, j, player):
    most_cells = get_most_cells(i, j, player, marks[player])
    for most_i, most_j in most_cells:
        dx = (1 if most_i > i else -1 if most_i < i else 0)
        dy = (1 if most_j > j else -1 if most_j < j else 0)
        curr_i, curr_j = i, j
        while abs(curr_i - most_i) + abs(curr_j - most_j) > 0:
            grid[curr_i][curr_j] = marks[player]
            curr_i += dx
            curr_j += dy

#This function generates the possible cells to be chosen 
def generate_possible_cells(player):
    global possible_cells
    possible_cells = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] != marks[player]:
                continue
            most_cells = get_most_cells(i, j, player, '.')
            for most_i, most_j in most_cells:
                possible_cells += [(most_i, most_j)]
    possible_cells = list(set(possible_cells))

#This function marks the possible cells in the grid
def mark_possible_cells():
    for i, j in possible_cells:
        grid[i][j] = '?'

#This function unmarks the possible cells in the grid
def unmark_possible_cells():
    for i, j in possible_cells:
        grid[i][j] = '.'

#This function clears the game structures
def grid_clear():
    global grid, count_cells
    grid = [['.'] * M for i in range(N)]
    grid[N//2][M//2-1] = grid[N//2-1][M//2] = marks[0]
    grid[N//2-1][M//2-1] = grid[N//2][M//2] = marks[1]
    count_cells = [0] * n_players

#This function reads a valid position input
def read_input():
    i, j = map(int, input('Enter the row index and column index: ').split())
    while not check_valid_position(i, j) or not check_empty(i, j) or not check_chosen(i, j):
        i, j = map(int, input('Enter a valid row index and a valid column index: ').split())
    return i, j


#MAIN FUNCTION
def play_game():
    print("Reversi Game!")
    print("Welcome...")
    print("============================")
    player = 0
    while True:
        #Generate the possible cells to be chosen 
        generate_possible_cells(player)
        #Mark the possible cells
        mark_possible_cells()
        #Prints the grid
        print_grid()
        #Unmark the possible cells
        unmark_possible_cells()
        #Read an input position from the player
        print('Player %s is playing now' % marks[player])
        #Keep the player if there is not an ability with the other player
        if not check_player_ability():
            print('Sorry, you can not play on this turn!')
            #Player number changes after each turn
            player = 1 - player 
            continue
        i, j = read_input()
        #Set the player mark in the input position
        set_cell(i, j, marks[player])
        #Switch the neighbor cells of the given cell
        switch_cells(i, j, player)
        #Calculates the total number of cells for each player
        calc_cells()
        #Check if the grid has a full state
        if check_full():
            #Prints the grid
            print_grid()
            #Announcement of the final statement
            if count_cells.count(max(count_cells)) == 1:
                idx_max_player = count_cells.index(max(count_cells))
                print('Congrats, Player %s is won!' % marks[idx_max_player])
            else:
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
