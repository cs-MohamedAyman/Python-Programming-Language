root_N = 3
N = root_N * root_N
mode, n_modes = 0, 35
similar_boxes, n_grids, graphs = [], [], []
grids, cpy_grids = [], []
symbols = ['.', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#This function checks if the given mode is valid or not 
def check_valid_mode(x):
    return 0 <= x < n_modes

#This function sets the configuration of Multi-Sudoku Game grids 
def set_config():
    global mode
    mode = int(input('Enter the mode index: '))
    while not check_valid_mode(mode):
        mode = int(input('Enter a valid mode index: '))

#This function prints the mode type
def print_mode_type(max_height, max_width, n_elements, curr_idx, grid_type):
    dashes  = ('-' * max_width * 8)
    spaces1 = (' ' * max_width * 3)
    spaces2 = (' ' * max_width * 4)
    max_width += max(0, max_width * (8 - n_elements - 1)) // n_elements
    print('+' + dashes + '+')
    print(('|' + spaces1 + '%d Grid(s) Multi-Sudoku' + spaces2 + '|') % grid_type)
    print('+' + dashes + '+')
    res = ''
    res += '\n' * ((max_height - len(graphs[curr_idx].split('\n')) + 1) // 2)
    for i in range(max_height):
        for j in range(n_elements):
            if i < len(graphs[curr_idx+j].split('\n'))-1: 
                res += graphs[curr_idx+j].split('\n')[i].center(max_width)
            else: 
                res += ' ' * max_width
        res += '\n'
    for j in range(n_elements):
        mode_num = str(curr_idx+j) if curr_idx+j > 9 else '0'+str(curr_idx+j)
        res += str('mode '+mode_num).center(max_width)
    curr_idx += n_elements
    return res

#This function prints the modes of Multi-Sudoku Game
def print_modes():
    idx, max_width = 0, 22
    print(print_mode_type(3, max_width, 1, idx, 1))
    idx += 1
    print(print_mode_type(5, max_width, 8, idx, 2))
    idx += 8
    print(print_mode_type(7, max_width, 8, idx, 3))
    idx += 8
    print(print_mode_type(7, max_width, 8, idx, 3))
    idx += 8
    print(print_mode_type(7, max_width, 8, idx, 4))
    idx += 8
    print(print_mode_type(7, max_width, 2, idx, 5))
    idx += 2

#This function contracts the modes of Multi-Sudoku Game grids 
def contract_modes():
    NL = '\n'
    #mode 00
    graphs.append('* * *'+NL+
                  '* * *'+NL+
                  '* * *'+NL)
    similar_boxes.append([])
    n_grids.append(1)
    #mode 01
    graphs.append('* * *    '+NL+
                  '* * *    '+NL+
                  '* * * * *'+NL+
                  '    * * *'+NL+
                  '    * * *'+NL)
    similar_boxes.append([(0, 8, 1, 0)])
    n_grids.append(2)
    #mode 02
    graphs.append('    * * *'+NL+
                  '    * * *'+NL+
                  '* * * * *'+NL+
                  '* * *    '+NL+
                  '* * *    '+NL)
    similar_boxes.append([(0, 6, 1, 2)])
    n_grids.append(2)
    #mode 03
    graphs.append('* * *  '+NL+
                  '* * *  '+NL+
                  '* * * *'+NL+
                  '  * * *'+NL+
                  '  * * *'+NL)
    similar_boxes.append([(0, 7, 1, 0), (0, 8, 1, 1)])
    n_grids.append(2)
    #mode 04
    graphs.append('  * * *'+NL+
                  '  * * *'+NL+
                  '* * * *'+NL+
                  '* * *  '+NL+
                  '* * *  '+NL)
    similar_boxes.append([(0, 6, 1, 1), (0, 7, 1, 2)])
    n_grids.append(2)
    #mode 05
    graphs.append('* * *    '+NL+
                  '* * * * *'+NL+
                  '* * * * *'+NL+
                  '    * * *'+NL)
    similar_boxes.append([(0, 5, 1, 0), (0, 8, 1, 3)])
    n_grids.append(2)
    #mode 06
    graphs.append('    * * *'+NL+
                  '* * * * *'+NL+
                  '* * * * *'+NL+
                  '* * *    '+NL)
    similar_boxes.append([(0, 3, 1, 2), (0, 6, 1, 5)])
    n_grids.append(2)
    #mode 07
    graphs.append('* * *  '+NL+
                  '* * * *'+NL+
                  '* * * *'+NL+
                  '  * * *'+NL)
    similar_boxes.append([(0, 4, 1, 0), (0, 5, 1, 1), (0, 7, 1, 3), (0, 8, 1, 4)])
    n_grids.append(2)
    #mode 08
    graphs.append('  * * *'+NL+
                  '* * * *'+NL+
                  '* * * *'+NL+
                  '* * *  '+NL)
    similar_boxes.append([(0, 3, 1, 1), (0, 4, 1, 2), (0, 6, 1, 4), (0, 7, 1, 5)])
    n_grids.append(2)
    #mode 09
    graphs.append('* * *        '+NL+
                  '* * *        '+NL+
                  '* * * * *    '+NL+
                  '    * * *    '+NL+
                  '    * * * * *'+NL+
                  '        * * *'+NL+
                  '        * * *'+NL)
    similar_boxes.append([(0, 8, 1, 0), (1, 8, 2, 0)])
    n_grids.append(3)
    #mode 10
    graphs.append('        * * *'+NL+
                  '        * * *'+NL+
                  '    * * * * *'+NL+
                  '    * * *    '+NL+
                  '* * * * *    '+NL+
                  '* * *        '+NL+
                  '* * *        '+NL)
    similar_boxes.append([(0, 6, 1, 2), (1, 6, 2, 2)])
    n_grids.append(3)
    #mode 11
    graphs.append('* * *    '+NL+
                  '* * *    '+NL+
                  '* * * *  '+NL+
                  '  * * *  '+NL+
                  '  * * * *'+NL+
                  '    * * *'+NL+
                  '    * * *'+NL)
    similar_boxes.append([(0, 7, 1, 0), (0, 8, 1, 1), (1, 7, 2, 0), (1, 8, 2, 1)])
    n_grids.append(3)
    #mode 12
    graphs.append('    * * *'+NL+
                  '    * * *'+NL+
                  '  * * * *'+NL+
                  '  * * *  '+NL+
                  '* * * *  '+NL+
                  '* * *    '+NL+
                  '* * *    '+NL)
    similar_boxes.append([(0, 6, 1, 1), (0, 7, 1, 2), (1, 6, 2, 1), (1, 7, 2, 2)])
    n_grids.append(3)
    #mode 13
    graphs.append('* * *        '+NL+
                  '* * * * *    '+NL+
                  '* * * * * * *'+NL+
                  '    * * * * *'+NL+
                  '        * * *'+NL)
    similar_boxes.append([(0, 5, 1, 0), (0, 8, 1, 3), (1, 5, 2, 0), (1, 8, 2, 3)])
    n_grids.append(3)
    #mode 14
    graphs.append('        * * *'+NL+
                  '    * * * * *'+NL+
                  '* * * * * * *'+NL+
                  '* * * * *    '+NL+
                  '* * *        '+NL)
    similar_boxes.append([(0, 3, 1, 2), (0, 6, 1, 5), (1, 3, 2, 2), (1, 6, 2, 5)])
    n_grids.append(3)
    #mode 15
    graphs.append('* * *    '+NL+
                  '* * * *  '+NL+
                  '* * * * *'+NL+
                  '  * * * *'+NL+
                  '    * * *'+NL)
    similar_boxes.append([(0, 4, 1, 0), (0, 5, 1, 1), (0, 7, 1, 3), (0, 8, 1, 4), (1, 4, 2, 0), (1, 5, 2, 1), (1, 7, 2, 3), (1, 8, 2, 4)])
    n_grids.append(3)
    #mode 16
    graphs.append('    * * *'+NL+
                  '  * * * *'+NL+
                  '* * * * *'+NL+
                  '* * * *  '+NL+
                  '* * *    '+NL)
    similar_boxes.append([(0, 3, 1, 1), (0, 4, 1, 2), (0, 6, 1, 4), (0, 7, 1, 5), (1, 3, 2, 1), (1, 4, 2, 2), (1, 6, 2, 4), (1, 7, 2, 5)])
    n_grids.append(3)
    #mode 17
    graphs.append('* * *    '+NL+
                  '* * *    '+NL+
                  '* * * * *'+NL+
                  '    * * *'+NL+
                  '* * * * *'+NL+
                  '* * *    '+NL+
                  '* * *    '+NL)
    similar_boxes.append([(0, 8, 1, 0), (1, 6, 2, 2)])
    n_grids.append(3)
    #mode 18
    graphs.append('    * * *'+NL+
                  '    * * *'+NL+
                  '* * * * *'+NL+
                  '* * *    '+NL+
                  '* * * * *'+NL+
                  '    * * *'+NL+
                  '    * * *'+NL)
    similar_boxes.append([(0, 6, 1, 2), (1, 8, 2, 0)])
    n_grids.append(3)
    #mode 19
    graphs.append('    * * *    '+NL+
                  '    * * *    '+NL+
                  '* * * * * * *'+NL+
                  '* * *   * * *'+NL+
                  '* * *   * * *'+NL)
    similar_boxes.append([(0, 6, 1, 2), (0, 8, 2, 0)])
    n_grids.append(3)
    #mode 20
    graphs.append('* * *   * * *'+NL+
                  '* * *   * * *'+NL+
                  '* * * * * * *'+NL+
                  '    * * *    '+NL+
                  '    * * *    '+NL)
    similar_boxes.append([(0, 8, 2, 0), (1, 6, 2, 2)])
    n_grids.append(3)
    #mode 21
    graphs.append('* * *  '+NL+
                  '* * *  '+NL+
                  '* * * *'+NL+
                  '  * * *'+NL+
                  '* * * *'+NL+
                  '* * *  '+NL+
                  '* * *  '+NL)
    similar_boxes.append([(0, 7, 1, 0), (0, 8, 1, 1), (1, 6, 2, 1), (1, 7, 2, 2)])
    n_grids.append(3)
    #mode 22
    graphs.append('  * * *'+NL+
                  '  * * *'+NL+
                  '* * * *'+NL+
                  '* * *  '+NL+
                  '* * * *'+NL+
                  '  * * *'+NL+
                  '  * * *'+NL)
    similar_boxes.append([(0, 6, 1, 1), (0, 7, 1, 2), (1, 7, 2, 0), (1, 8, 2, 1)])
    n_grids.append(3)
    #mode 23
    graphs.append('    * * *    '+NL+
                  '* * * * * * *'+NL+
                  '* * * * * * *'+NL+
                  '* * *   * * *'+NL)
    similar_boxes.append([(0, 3, 1, 2), (0, 5, 1, 5), (0, 6, 2, 0), (0, 8, 2, 3)])
    n_grids.append(3)
    #mode 24
    graphs.append('* * *   * * *'+NL+
                  '* * * * * * *'+NL+
                  '* * * * * * *'+NL+
                  '    * * *    '+NL)
    similar_boxes.append([(0, 5, 2, 0), (0, 8, 2, 3), (1, 3, 2, 2), (1, 6, 2, 5)])
    n_grids.append(3)
    #mode 25
    graphs.append('    * * *    '+NL+
                  '    * * *    '+NL+
                  '* * * * * * *'+NL+
                  '* * *   * * *'+NL+
                  '* * * * * * *'+NL+
                  '    * * *    '+NL+
                  '    * * *    '+NL)
    similar_boxes.append([(0, 6, 1, 2), (0, 8, 2, 0), (1, 8, 3, 0), (2, 6, 3, 2)])
    n_grids.append(4)
    #mode 26
    graphs.append('  * * *    '+NL+
                  '  * * * * *'+NL+
                  '* * * * * *'+NL+
                  '* * * * * *'+NL+
                  '* * * * *  '+NL+
                  '    * * *  '+NL)
    similar_boxes.append([(0, 5, 1, 0), (0, 6, 2, 1), (0, 7, 2, 2), (0, 8, 1, 3), (3, 0, 2, 5), (3, 1, 1, 6), (3, 2, 1, 7), (3, 3, 2, 8)])
    n_grids.append(4)
    #mode 27
    graphs.append('    * * *  '+NL+
                  '* * * * *  '+NL+
                  '* * * * * *'+NL+
                  '* * * * * *'+NL+
                  '  * * * * *'+NL+
                  '  * * *    '+NL)
    similar_boxes.append([(0, 3, 1, 2), (0, 6, 1, 5), (0, 7, 2, 0), (0, 8, 2, 1), (3, 0, 1, 7), (3, 1, 1, 8), (3, 2, 2, 3), (3, 3, 2, 5)])
    n_grids.append(4)
    #mode 28
    graphs.append('    * * *    '+NL+
                  '* * * * * * *'+NL+
                  '* * * * * * *'+NL+
                  '* * * * * * *'+NL+
                  '    * * *    '+NL+
                  '    * * *    '+NL)
    similar_boxes.append([(1, 2, 0, 3), (1, 5, 0, 6), (1, 8, 3, 0), (2, 0, 0, 5), (2, 3, 0, 8), (2, 6, 3, 2)])
    n_grids.append(4)
    #mode 29
    graphs.append('    * * *    '+NL+
                  '    * * *    '+NL+
                  '* * * * * * *'+NL+
                  '* * * * * * *'+NL+
                  '* * * * * * *'+NL+
                  '    * * *    '+NL)
    similar_boxes.append([(1, 2, 0, 6), (1, 5, 3, 0), (1, 8, 3, 3), (2, 0, 0, 8), (2, 3, 3, 2), (2, 6, 3, 5)])
    n_grids.append(4)
    #mode 30
    graphs.append('  * * *    '+NL+
                  '  * * *    '+NL+
                  '* * * * * *'+NL+
                  '* * * * * *'+NL+
                  '* * * * * *'+NL+
                  '  * * *    '+NL+
                  '  * * *    '+NL)
    similar_boxes.append([(0, 6, 1, 1), (0, 7, 1, 2), (0, 8, 2, 0), (3, 0, 1, 7), (3, 1, 1, 8), (3, 2, 2, 6)])
    n_grids.append(4)
    #mode 31
    graphs.append('    * * *  '+NL+
                  '    * * *  '+NL+
                  '* * * * * *'+NL+
                  '* * * * * *'+NL+
                  '* * * * * *'+NL+
                  '    * * *  '+NL+
                  '    * * *  '+NL)
    similar_boxes.append([(0, 6, 1, 2), (0, 7, 2, 0), (0, 8, 2, 1), (3, 0, 1, 8), (3, 1, 2, 6), (3, 2, 2, 7)])
    n_grids.append(4)
    #mode 32
    graphs.append('  * * *  '+NL+
                  '* * * * *'+NL+
                  '* * * * *'+NL+
                  '* * * * *'+NL+
                  '  * * *  '+NL)
    similar_boxes.append([(0, 3, 1, 1), (0, 4, 1, 2), (0, 4, 2, 0), (0, 5, 2, 1), (1, 2, 2, 0), 
                          (3, 0, 1, 4), (3, 1, 1, 5), (3, 1, 2, 3), (3, 2, 2, 4), (1, 8, 2, 6),
                          (1, 4, 0, 6), (1, 4, 3, 0), (0, 6, 3, 0),
                          (2, 4, 0, 8), (2, 4, 3, 2), (0, 8, 3, 2),
                          (0, 7, 3, 1), (1, 5, 2, 3), (0, 7, 1, 5), (0, 7, 2, 3), (1, 5, 3, 1), (2, 3, 3, 1)])
    n_grids.append(4)
    #mode 33
    graphs.append('* * *   * * *'+NL+
                  '* * *   * * *'+NL+
                  '* * * * * * *'+NL+
                  '    * * *    '+NL+
                  '* * * * * * *'+NL+
                  '* * *   * * *'+NL+
                  '* * *   * * *'+NL)
    similar_boxes.append([(0, 8, 2, 0), (1, 6, 2, 2), (2, 6, 3, 2), (2, 8, 4, 0)])
    n_grids.append(5)
    #mode 34
    graphs.append('  * * *  '+NL+
                  '* * * * *'+NL+
                  '* * * * *'+NL+
                  '* * * * *'+NL+
                  '  * * *  '+NL)
    similar_boxes.append([(0, 0, 1, 1), (0, 3, 1, 4), (0, 6, 1, 7), (0, 1, 1, 2), (0, 4, 1, 5), (0, 7, 1, 8), 
                          (0, 0, 2, 3), (0, 1, 2, 4), (0, 2, 2, 5), (0, 3, 2, 6), (0, 4, 2, 7), (0, 5, 2, 8), 
                          (0, 1, 3, 0), (0, 4, 3, 3), (0, 7, 3, 6), (0, 2, 3, 1), (0, 5, 3, 4), (0, 8, 3, 7), 
                          (0, 3, 4, 0), (0, 4, 4, 1), (0, 5, 4, 2), (0, 6, 4, 3), (0, 7, 4, 4), (0, 8, 4, 5),
                          (1, 2, 3, 0), (1, 5, 3, 3), (1, 8, 3, 6), (2, 6, 4, 0), (2, 7, 4, 1), (2, 8, 4, 2),
                          (2, 3, 1, 1), (2, 4, 1, 2), (2, 4, 3, 0), (2, 5, 3, 1),
                          (4, 3, 1, 7), (4, 4, 1, 8), (4, 4, 3, 6), (4, 5, 3, 7),
                          (1, 1, 2, 3), (1, 4, 2, 6), (1, 4, 4, 0), (1, 7, 4, 3),
                          (3, 1, 2, 5), (3, 4, 2, 8), (3, 4, 4, 2), (3, 7, 4, 5),
                          (4, 0, 1, 4), (4, 1, 1, 5), (4, 1, 3, 3), (4, 2, 3, 4),
                          (2, 6, 1, 4), (2, 7, 1, 5), (2, 7, 3, 3), (2, 8, 3, 4),
                          (1, 2, 1, 4), (1, 5, 1, 7), (1, 5, 4, 1), (1, 8, 4, 4),
                          (3, 0, 1, 4), (3, 3, 1, 7), (3, 3, 4, 1), (3, 6, 4, 4)])
    n_grids.append(5)

#This function prints the grids of Multi-Sudoku Game as the game progresses
def print_grid(grid_idx=0):
    print(('-' * (N*3)) + ('---' * root_N) + '-')
    for i in range(N):
        print(end='|  ')
        for j in range(N):
            if j % root_N == 0 and j > 0:
                print('|  ', end='')
            print(symbols[grids[grid_idx][i][j]], end='  ')
        print(end='|')
        print()
        if i % root_N == root_N - 1:
            print(('-' * (N*3)) + ('---' * root_N) + '-')

#This function prints the grids of Multi-Sudoku Game as the game progresses
def print_grids():
    for grid_idx in range(n_grids[mode]):
        print_grid(grid_idx)

#This function clears the game structures
def grid_clear():
    global grids, cpy_grids
    grids = [[[0] * N for j in range(N)] for i in range(n_grids[mode])]
    cpy_grids = [[[0] * N for j in range(N)] for i in range(n_grids[mode])]
