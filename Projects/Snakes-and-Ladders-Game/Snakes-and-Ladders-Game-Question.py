import random
N, M = 10, 10
n_players, n_components = 2, 6
marks = ['X', 'O']
max_cell_width = max(8, n_players * 2 + 2)
ladder_symbol, snake_symbol = 'L', 'S'
grid, player_position, snakes, ladders = [], [], [], []

#This function converts the given indices into position
def convert_indices_to_position(i, j):
    pass

#This function converts the given position into indices
def convert_position_to_indices(p):
    pass

#This function prints the grid of Snakes and Ladders as the game progresses
def print_grid():
    for i in range(n_players):
        print('Player %d: %c  ' % (i+1, marks[i]), end='')
        if i < n_players-1:
            print('vs  ', end='')
    print()
    print('-' * max_cell_width * M + '-')
    for i in range(N):
        print('|', end='')
        for j in range(M):
            cell, symbol = '', ''
            p = convert_indices_to_position(i, j)
            for k in range(n_components):
                if p == ladders[k][0] or p == ladders[k][1]:
                    symbol = ladder_symbol+str(k+1)
                    break
                if p == snakes[k][0] or p == snakes[k][1]:
                    symbol = snake_symbol+str(k+1)
                    break
            cell += symbol + ' ' * (2 - len(symbol))
            cell += ' ' * (max_cell_width - 2 - 3 - 1)
            cell += ' ' * (3 - len(str(p))) + str(p)
            print(cell + '|', end='')
        print()
        print('|', end='')
        for j in range(M):
            cell = ''
            for k in range(n_players):
                p1, p2 = convert_position_to_indices(player_position[k])
                if (p1, p2) == (i, j): cell += ' ' + marks[k]
            cell += ' ' * (max_cell_width - 1 - len(cell))
            print(cell + '|', end='')
        print()
        print('-' * max_cell_width * M + '-')
    for i in range(n_players):
        print('Player %c in %d'% (marks[i], player_position[i]))
    print('-' * max_cell_width * M + '-')

#This function checks if the given player reach the end of the game or not 
def check_win(player):
    pass

#This function generate a random dice face
def generate_dice_face():
    pass

#This function prints the given dice face
def print_dice_face(i):
    s = ''
    if i == 1:
        s += ' _____ \n'
        s += '|     |\n'
        s += '|  *  |\n'
        s += '|_____|\n'
    if i == 2:
        s += ' _____ \n'
        s += '|    *|\n'
        s += '|     |\n'
        s += '|*____|\n'
    if i == 3:
        s += ' _____ \n'
        s += '|    *|\n'
        s += '|  *  |\n'
        s += '|*____|\n'
    if i == 4:
        s += ' _____ \n'
        s += '|*   *|\n'
        s += '|     |\n'
        s += '|*___*|\n'
    if i == 5:
        s += ' _____ \n'
        s += '|*   *|\n'
        s += '|  *  |\n'
        s += '|*___*|\n'
    if i == 6:
        s += ' _____ \n'
        s += '|*   *|\n'
        s += '|*   *|\n'
        s += '|*___*|\n'
    return s

#This function checks if given face is valid or not 
def check_valid_face(i):
    pass

#This function moves the given player by the given value
def move_player(player, moves):
    pass

#This function generates snakes and ladders in the grid
def generate_snakes_and_ladders(symbol):
    n_mid, m_mid = N//2, M//2
    areas_beg = [(1, 1, n_mid-1, m_mid-1),             (1, m_mid, n_mid-1, M-2), \
                 (n_mid, 1, N-2, m_mid-1),             (n_mid, m_mid, N-2, M-2), \
                 (n_mid-2, m_mid-2, n_mid-2, m_mid+1), (0, m_mid-2, 0, m_mid+1)]
    areas_end = [(1, 1, n_mid-1, m_mid-1),             (1, m_mid, n_mid-1, M-2), \
                 (n_mid, 1, N-2, m_mid-1),             (n_mid, m_mid, N-2, M-2), \
                 (N-1, m_mid-2, N-1, m_mid+1),         (n_mid+1, m_mid-2, n_mid+1, m_mid+1)]
    for i in range(n_components):
        xb1, yb1, xe1, ye1 = areas_beg[i]
        xb2, yb2, xe2, ye2 = areas_end[i]
        x1, y1 = random.randint(xb1, xe1), random.randint(yb1, ye1)
        x2, y2 = random.randint(xb2, xe2), random.randint(yb2, ye2)
        while x1 == x2 or y1 == y2 or abs(x1 - x2) + abs(y1 - y2) <= int(min(N**.5, M**.5)) or \
              grid[x1][y1] != '.' or grid[x2][y2] != '.':
            x1, y1 = random.randint(xb1, xe1), random.randint(yb1, ye1)
            x2, y2 = random.randint(xb2, xe2), random.randint(yb2, ye2)
        grid[x1][y1] = symbol
        grid[x2][y2] = symbol
        p1 = convert_indices_to_position(x1, y1)
        p2 = convert_indices_to_position(x2, y2)
        if symbol == ladder_symbol: ladders[i] = (min(p1, p2), max(p1, p2))
        if symbol == snake_symbol : snakes[i]  = (min(p1, p2), max(p1, p2))

#This function gets the movement value of the given position
def get_entity_value(p):
    pass

#This function clears the game structures
def grid_clear():
    pass

#This function reads a valid input
def read_input():
    i = input('Choose the dice face [A B C D E F]: ')
    while not check_valid_face(i):
        i = input('Choose a valid dice face [A B C D E F]: ')
    return i


#MAIN FUNCTION
def play_game():
    print("Snakes and Ladders Game!")
    print("Welcome...")
    print("============================")
    player = 0
    while True:
        #Prints the grid
        print_grid()
        #Read an input dice face from the player
        print('Player %s is playing now' % marks[player])
        i = read_input()
        #Generate a dice face
        dice_face = generate_dice_face()
        print(print_dice_face(dice_face))
        #Move the player position
        move_player(player, dice_face)
        #Get the movement value if there is an entity
        entity_value = get_entity_value(player_position[player])
        if entity_value > 0:
            #Prints the grid
            print_grid()
            print('Player %s face a ladder, there is a movement from %d to %d' % \
                  (marks[player], player_position[player], player_position[player]+entity_value))
            #Move the player position
            move_player(player, entity_value)
        if entity_value < 0:
            #Prints the grid
            print_grid()
            print('Player %s face a snake, there is a movement from %d to %d' % \
                  (marks[player], player_position[player], player_position[player]+entity_value))
            #Move the player position
            move_player(player, entity_value)
        #Check if the state of the grid has a win state
        if check_win(player):
            #Prints the grid
            print_grid()
            print('Congrats, Player %s is won!' % marks[player])
            break
        #Player number changes after each turn
        player = (player + 1) % n_players


while True:
    grid_clear()
    generate_snakes_and_ladders(ladder_symbol)
    generate_snakes_and_ladders(snake_symbol)
    play_game()
    c = input('Play Again [Y/N] ')
    if c not in 'yY':
        break
