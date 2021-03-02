N, M = 5, 5
n_players = 2
marks = ['X', 'O']
count_boxes, grid, horizontal_grid, vertical_grid = [], [], [], []

#This function prints the grid of Dots-and-Boxes as the game progresses
def print_grid():
    for i in range(n_players):
        print('Player %d: %c ' % (i+1, marks[i]), end='')
        if i < n_players-1:
            print('vs ', end='')
    print()
    print('--' + '------' * (M-1))
    for i in range(N):
        print(' . ', end = '')
        for j in range(M):
            if horizontal_grid[i][j]:
                print('---', end = '')
            else:
                print('   ', end = '')
            if j < M-1:
                print(' . ', end = '')
        print()
        for j in range(M+1):
            if vertical_grid[i][j]:
                print(' |  ', end = '')
            else:
                print('    ', end = '')
            if i < N-1 and j < M-1:
                print(grid[i][j] if grid[i][j] != '.' else ' ', end='')
            print(' ', end = '')
        print()
    for i in range(n_players):
        print('Player %c is %d'% (marks[i], count_boxes[i]))
    print('--' + '------' * (M-1))

#This function checks if the grid is full or not
def check_complete():
    pass

#This function checks if given cell is empty in the horizontal grid or not 
def check_empty_horizontal_side(i, j):
    pass

#This function checks if given cell is empty in the vertical grid or not 
def check_empty_vertical_side(i, j):
    pass

#This function checks if given side is empty or not 
def check_empty_side(i1, j1, i2, j2):
    pass

#This function checks if given position is valid in the grid or not 
def check_valid_position(i, j):
    pass

#This function checks if given side is valid or not 
def check_valid_side(i1, j1, i2, j2):
    pass

#This function sets a side to a cell in the horizontal grid
def set_horizontal_side(i, j):
    pass

#This function sets a side to a cell in the vertical grid
def set_vertical_side(i, j):
    pass

#This function sets a side to a cell in the grid
def set_side(i1, j1, i2, j2):
    pass

#This function checks if the given box is complete or not
def is_complete_box(i, j):
    pass

#This function sets a value to a cell in the grid as a complete box
def set_box(i, j, player):
    pass

#This function checks and sets a box to a cell in the grid as a complete box
def set_neighbor_box(i1, j1, i2, j2, player):
    pass

#This function checks and sets the neighbor boxes in the grid as a complete boxes
def set_neighbor_boxes(i1, j1, i2, j2, player):
    pass

#This function arranges the points of the side
def arrange_side_points(i1, j1, i2, j2):
    pass

#This function clears the grid
def grid_clear():
    pass


#MAIN FUNCTION
def play_game():
    print("Dots-and-Boxes Game!")
    print("Welcome...")
    print("============================")
    player = 0
    while True:
        #Prints the grid
        print_grid()
        #Read an input from the player
        print('Player %s' % marks[player])
        i1, j1, i2, j2 = map(int, input('Enter the two points of the side: ').split())
        i1, j1, i2, j2 = arrange_side_points(i1, j1, i2, j2)
        while not check_valid_position(i1, j1) or not check_valid_position(i2, j2) or \
              not check_valid_side(i1, j1, i2, j2) or not check_empty_side(i1, j1, i2, j2):
            i1, j1, i2, j2 = map(int, input('Enter a valid two points of the side: ').split())
            i1, j1, i2, j2 = arrange_side_points(i1, j1, i2, j2)
        #Set the input position with the mark
        set_side(i1, j1, i2, j2)
        #Set the neighbor boxes with the mark
        box_complete = set_neighbor_boxes(i1, j1, i2, j2, player)
        #Check if the state of the grid has a complete state
        if check_complete():
            #Prints the grid
            print_grid()
            #Announcement of the final statement
            if count_boxes.count(max(count_boxes)) == 1:
                print('Congrats, Player %s is won!' % marks[count_boxes.index(max(count_boxes))])
            else:
                print("Woah! That's a tie!")
            break
        if not box_complete:
            #Player number changes after each turn
            player = (player + 1) % n_players


while True:
	grid_clear()
	play_game()
	c = input('Play Again [Y/N] ')
	if c not in 'yY':
		break