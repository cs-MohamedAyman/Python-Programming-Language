N, M = 8, 8
n_players = 2
marks = [['B', 'W'], ['KB', 'KW']]
count_cells, grid, is_king, possible_cells = [], [], [], []

#This function prints the grid of Draughts as the game progresses
def print_grid():
    print("Player 1: %c  vs  Player 2: %c" % (marks[0][0], marks[0][1]))
    print('--' + '--' * 2 * M + '--')
    for i in range(N):
        print(end='|  ')
        for j in range(M):
            cell = str(grid[i][j]) + (' ' * (2 - len(grid[i][j])))
            print(cell, end='  ')
        print(end='|')
        print()
        print('--' + '--' * 2 * M + '--')
    for i in range(n_players):
        print('Player %c has %d cells'% (marks[0][i], count_cells[i]))
    print('--' + '------' * (M-1))

#This function checks if the game has a win state or not
def check_win():
    pass

#This function checks if the game has a tie state or not
def check_player_ability():
    pass

#This function checks if given cell is empty or not 
def check_empty(i, j):
    pass

#This function checks if given position is valid or not 
def check_valid_position(i, j):
    pass

#This function checks if given cell is chosen or not 
def check_chosen(i1, j1, i2, j2):
    pass

#This function sets the given mark to the given cell
def set_cell(i, j, mark):
    pass

#This function moves the given player form the source cell to the target cell
def move_cell(i1, j1, i2, j2, player):
    pass

#This function generates the possible cells to be chosen in the attack case
def generate_possible_cells_attack_case(player):
    pass

#This function generates the possible cells to be chosen in the defence case
def generate_possible_cells_defence_case(player):
    pass

#This function generates the possible cells to be chosen 
def generate_possible_cells(player):
    global possible_cells
    possible_cells = []
    generate_possible_cells_attack_case(player)
    if possible_cells: return
    generate_possible_cells_defence_case(player)
    possible_cells = list(set(possible_cells))

#This function marks the possible cells in the grid
def mark_possible_cells():
    pass

#This function unmarks the possible cells in the grid
def unmark_possible_cells():
    pass

#This function clears the game structures
def grid_clear():
    pass

#This function reads a valid position input
def read_input(player):
    i1, j1, i2, j2 = map(int, input('Enter the source and target points: ').split())
    while not check_valid_position(i1, j1) or not check_valid_position(i2, j2) or \
          check_empty(i1, j1) or not check_empty(i2, j2) or not check_chosen(i1, j1, i2, j2):
        i1, j1, i2, j2 = map(int, input('Enter a valid source and target points: ').split())
    return i1, j1, i2, j2


#MAIN FUNCTION
def play_game():
    print("Draughts Game!")
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
        print('Player %s is playing now' % marks[0][player])
        #Keep the player if there is not an ability with the other player
        if not check_player_ability():
            print("Woah! That's a tie!")
            break
        #Read an input position from the player
        i1, j1, i2, j2 = read_input(player)
        #Set the player mark in the input position
        move_cell(i1, j1, i2, j2, player)
        #Check if the grid has a win state
        if check_win():
            #Prints the grid
            print_grid()
            print('Congrats, Player %s is won!' % marks[0][player])
            break
        #Player number changes after each turn
        player = 1 - player 


while True:
	grid_clear()
	play_game()
	c = input('Play Again [Y/N] ')
	if c not in 'yY':
		break
