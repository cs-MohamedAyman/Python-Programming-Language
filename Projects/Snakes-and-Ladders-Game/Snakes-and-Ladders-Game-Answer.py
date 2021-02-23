import random
N, M = 10, 10
ladder_symbol, snake_symbol = 'L', 'S'
grid, player_position, snakes, ladders = [], [], [], []

#This function prints the grid of Snakes and Ladders as the game progresses
def print_grid():
    print("Player 1: X  vs  Player 2: O")
    print('-------' * M + '-')
    for i in range(N):
        row_res = ''
        row_res += '|'
        for j in range(M):
            p1, p2 = convert_position_to_indices(player_position[0])
            row_res += 'X  ' if (p1, p2) == (i, j) else '   '
            p = convert_indices_to_position(i, j)
            row_res += '  ' + str(p) if p < 10 else ' ' + str(p) if p < 100 else str(p)
            row_res += '|'
        row_res += '\n|'
        for j in range(M):
            symbol = '  '
            p = convert_indices_to_position(i, j)
            if grid[i][j] == ladder_symbol:
                for k in range(6):
                    if p == ladders[k][0] or p == ladders[k][1]:
                        symbol = ladder_symbol+str(k+1)
                        break
            if grid[i][j] == snake_symbol:
                for k in range(6):
                    if p == snakes[k][0] or p == snakes[k][1]:
                        symbol = snake_symbol+str(k+1)
                        break
            row_res += symbol + ' '
            p1, p2 = convert_position_to_indices(player_position[1])
            row_res += '  O' if (p1, p2) == (i, j) else '   '
            row_res += '|'
        print(row_res)
        print('-------' * M + '-')
    print('Player X in', player_position[0])
    print('Player O in', player_position[1])
    print('-------' * M + '-')

#This function checks if the given player reach the end of the game or not 
def check_win(player):
    return player_position[player] >= N * M

#This function generate a random dice face
def generate_dice_face():
	return random.randint(1, 6)

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
	return i.lower() in 'abcdef'

#This function converts the given indices into position
def convert_indices_to_position(i, j):
    p = (N - i - 1) * M
    if i % 2 == N % 2:
        p += M - j
    else:
        p += j + 1
    return p

#This function converts the given position into indices
def convert_position_to_indices(p):
    i = N - (p - 1) // M - 1
    if i % 2 == N % 2:
        j = (M - p % M) % M
    else:
        j = (p % M - 1 + M) % M
    return i, j

#This function moves the given player by the given value
def move_player(player, moves):
    player_position[player] += moves
    player_position[player] = min(N * M, player_position[player])

#This function generates snakes and ladders in the grid
def generate_snakes_and_ladders(symbol):
    n_mid, m_mid = N//2, M//2
    areas_beg = [(1, 1, n_mid-1, m_mid-1), (1, m_mid, n_mid-1, M-2), (n_mid, 1, N-2, m_mid-1), \
                 (n_mid, m_mid, N-2, M-2), (n_mid-2, m_mid-2, n_mid-2, m_mid+1), (0, m_mid-2, 0, m_mid+1)]
    areas_end = [(1, 1, n_mid-1, m_mid-1), (1, m_mid, n_mid-1, M-2), (n_mid, 1, N-2, m_mid-1), \
                 (n_mid, m_mid, N-2, M-2), (N-1, m_mid-2, N-1, m_mid+1), (n_mid+1, m_mid-2, n_mid+1, m_mid+1)]
    for i in range(6):
        xb1, yb1, xe1, ye1 = areas_beg[i]
        xb2, yb2, xe2, ye2 = areas_end[i]
        x1, y1 = random.randint(xb1, xe1), random.randint(yb1, ye1)
        x2, y2 = random.randint(xb2, xe2), random.randint(yb2, ye2)
        while x1 == x2 or y1 == y2 or abs(x1 - x2) + abs(y1 - y2) <= 2 or \
              grid[x1][y1] != '.' or grid[x2][y2] != '.':
            x1, y1 = random.randint(xb1, xe1), random.randint(yb1, ye1)
            x2, y2 = random.randint(xb2, xe2), random.randint(yb2, ye2)
        grid[x1][y1] = symbol
        grid[x2][y2] = symbol
        p1 = convert_indices_to_position(x1, y1)
        p2 = convert_indices_to_position(x2, y2)
        if symbol == ladder_symbol: ladders[i] = (min(p1, p2), max(p1, p2))
        if symbol == snake_symbol : snakes[i]  = (min(p1, p2), max(p1, p2))

#This function gets the plus value of the given position
def get_ladder_plus_value(p):
    for p1, p2 in ladders:
        if p == p1:
            return p2 - p1
    return 0
    
#This function gets the minus value of the given position
def get_snake_minus_value(p):
    for p1, p2 in snakes:
        if p == p2:
            return p1 - p2
    return 0

#This function clears the grid
def grid_clear():
    global grid, player_position, snakes, ladders
    grid = [['.' for i in range(M)] for j in range(N)]
    player_position = [0] * 2
    snakes, ladders = [(0, 0)] * 6, [(0, 0)] * 6


#MAIN FUNCTION
def play_game():
    print("Snakes and Ladders Game!")
    print("Welcome...")
    print("============================")
    player = 0
    while True:
        #Prints the grid
        print_grid()
        #Set mark value based on the player
        mark = 'X' if player == 0 else 'O'
        #Read an input from the player
        print('Player %s' % mark)
        i = input('Choose the dice face [A B C D E F]: ')
        while not check_valid_face(i):
            i = input('Choose a valid dice face [A B C D E F]: ')
        #Generate a dice face
        dice_face = generate_dice_face()
        print(print_dice_face(dice_face))
        #Move the player position
        move_player(player, dice_face)
        #Get the plus value if there is a ladder
        plus_value = get_ladder_plus_value(player_position[player])
        if plus_value > 0:
            #Prints the grid
            print_grid()
            print('Player %s face a ladder, there is a movement from %d to %d' % \
                  (mark, player_position[player], player_position[player]+plus_value))
            #Move the player position
            move_player(player, plus_value)
        #Get the minus value if there is a snake
        minus_value = get_snake_minus_value(player_position[player])        
        if minus_value < 0:
            #Prints the grid
            print_grid()
            print('Player %s face a snake, there is a movement from %d to %d' % \
                  (mark, player_position[player], player_position[player]+minus_value))
            #Move the player position
            move_player(player, minus_value)
        #Check if the state of the grid has a win state
        if check_win(player):
            #Prints the grid
            print_grid()
            print('Congrats, Player %s is won!' % mark)
            break
        #Player number changes after each turn
        player = 1 - player 


while True:
    grid_clear()
    generate_snakes_and_ladders(ladder_symbol)
    generate_snakes_and_ladders(snake_symbol)
    play_game()
    c = input('Play Again [Y/N] ')
    if c not in 'yY':
        break
