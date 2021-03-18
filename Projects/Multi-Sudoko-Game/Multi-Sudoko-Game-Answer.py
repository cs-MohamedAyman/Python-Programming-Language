import random
root_N = 3
N = root_N * root_N
mode = 33
grids, cpy_grids = [], []
similar_boxes, n_grids, graphs = [], [], []
symbols = ['.', '1', '2', '3', '4', '5', '6', '7', \
           '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G']

#This function sets the configuration of Sudoku Game grids 
def set_config():
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

#This function checks if the given grid has a win state or not
def check_win_grid(grid_idx):
    #Check if all rows are not full, the game is still running
    for i in range(N):
        s = set()
        for j in range(N):
            s.add(grids[grid_idx][i][j])
        if len(s) != N or 0 in s:
            return False
    #Check if all columns are not full, the game is still running
    for i in range(N):
        s = set()
        for j in range(N):
            s.add(grids[grid_idx][j][i])
        if len(s) != N or 0 in s:
            return False
    #Check if all boxes are not full, the game is still running
    for i in range(0, N, root_N):
        for j in range(0, N, root_N):
            s = set()
            for k in range(i, i+root_N):
                for w in range(j, j+root_N):
                    s.add(grids[grid_idx][k][w])
            if len(s) != N or 0 in s:
                return False
    #Otherwise, there is a win state in the game, 
    #if all cases above not reached		
    return True

#This function checks if the game has a win state or not
def check_win():
    for grid_idx in range(n_grids[mode]):
        if not check_win_grid(grid_idx):
            return False
    return True

#This function checks if the given position is valid or not 
def check_valid_position(i, j):
    return 0 <= i < N and 0 <= j < N

#This function checks if the given grid index is valid or not 
def check_valid_grid_index(grid_idx=0):
    return 0 <= grid_idx < n_grids[mode]

#This function checks if the given cell is empty or not 
def check_empty_cell(i, j, grid_idx=0):
    return grids[grid_idx][i][j] == 0

#This function checks if the given cell is original or not
def check_original_cell(i, j, grid_idx=0):
    return cpy_grids[grid_idx][i][j] != 0

#This function checks if the given value is valid with the given cell
def check_valid_value(i, j, v, grid_idx=0):
	#Check delete case
    if v == 0:
        return True
	#Check invalid value
    if v < 1 or v > N:
        return False
	#Check duplicate in all rows
    for k in range(N):
        if grids[grid_idx][i][k] == v:
            return False
	#Check duplicate in all columns
    for k in range(N):
        if grids[grid_idx][k][j] == v:
            return False
	#Check duplicate in all boxes
    b, e = i//root_N*root_N, j//root_N*root_N
    for k in range(b, b+root_N):
        for w in range(e, e+root_N):
            if grids[grid_idx][k][w] == v:
                return False
    #Otherwise, the given value is valid,
    #if all cases above not reached		
    return True

#This function converts the given position in the grid into a box number
def cvt_grid_pos_to_box(i, j):
    return i // root_N * root_N + j // root_N

#This function converts the given box number into a position index in the grid
def cvt_box_to_grid_pos(x):
    return x // root_N * root_N, x % root_N * root_N

#This function copies a cell from the givne source grid to the given target grid
def check_valid_value_cell(grid_idx_s, box_idx_s, grid_idx_t, box_idx_t, i, j, v):
    i_s, j_s = cvt_box_to_grid_pos(box_idx_s)
    i_t, j_t = cvt_box_to_grid_pos(box_idx_t)
    if i_s <= i < i_s+root_N and j_s <= j < j_s+root_N:
        step_i = i_t - i_s
        step_j = j_t - j_s
        return check_valid_value(i+step_i, j+step_j, v, grid_idx_t)
    return True

#This function checks if the given value is valid with the shared boxes in the other grids
def check_valid_value_in_shared_boxes(i, j, v, grid_idx=0):
    res = check_valid_value(i, j, v, grid_idx)
    for grid_i, box_i, grid_j, box_j in similar_boxes[mode]:
        if grid_idx == grid_i:
            res &= check_valid_value_cell(grid_i, box_i, grid_j, box_j, i, j, v)
        if grid_idx == grid_j:
            res &= check_valid_value_cell(grid_j, box_j, grid_i, box_i, i, j, v)
    return res

#This function copies a cell from the givne source grid to the given target grid
def cpy_cell(grid_idx_s, box_idx_s, grid_idx_t, box_idx_t, i, j, set_original=False):
    i_s, j_s = cvt_box_to_grid_pos(box_idx_s)
    i_t, j_t = cvt_box_to_grid_pos(box_idx_t)
    if i_s <= i < i_s+root_N and j_s <= j < j_s+root_N:
        step_i = i_t - i_s
        step_j = j_t - j_s
        grids[grid_idx_t][i+step_i][j+step_j] = grids[grid_idx_s][i][j]
        if set_original:
            cpy_grids[grid_idx_t][i+step_i][j+step_j] = cpy_grids[grid_idx_s][i][j]

#This function copies the shared boxes in the other grids
def cpy_cell_in_shared_boxes(i, j, v, grid_idx=0):
    for grid_i, box_i, grid_j, box_j in similar_boxes[mode]:
        if grid_idx == grid_i:
            cpy_cell(grid_i, box_i, grid_j, box_j, i, j)
        if grid_idx == grid_j:
            cpy_cell(grid_j, box_j, grid_i, box_i, i, j)

#This function sets the given value to the given cell
def set_cell(i, j, v, grid_idx=0):
    grids[grid_idx][i][j] = v
    cpy_cell_in_shared_boxes(i, j, v, grid_idx)

#This function solves the grid
def solve_grid(i, j, grid_idx=0):
    if j == N:
        i += 1
        j = 0
    if i == N:
        return True
    if check_original_cell(i, j, grid_idx):
        return solve_grid(i, j+1, grid_idx)
    for k in range(1, N+1):
        if check_valid_value_in_shared_boxes(i, j, k, grid_idx):
            grids[grid_idx][i][j] = k
            cpy_grids[grid_idx][i][j] = k
            if solve_grid(i, j+1, grid_idx):
                return True
            grids[grid_idx][i][j] = 0
            cpy_grids[grid_idx][i][j] = 0
    return False

#This function gets the similar boxes the other grids
def get_similar_boxes(box_idx, grid_idx=0):
    res = []
    for grid_i, box_i, grid_j, box_j in similar_boxes[mode]:
        if grid_idx == grid_i and box_idx == box_i:
            res += [(grid_j, box_j)]
        if grid_idx == grid_j and box_idx == box_j:
            res += [(grid_i, box_i)]
    return res    

#This function copies the given box in the shared boxes in the other grids
def cpy_box_in_shared_boxes(box_idx, shared_boxes, grid_idx=0, set_original=False):
    for grid_k, box_k in shared_boxes:
        a, b = cvt_box_to_grid_pos(box_idx)
        for i in range(a, a+root_N):
            for j in range(b, b+root_N):
                cpy_cell(grid_idx, box_idx, grid_k, box_k, i, j, True)

#This function checks if the given box is empty or not
def is_empty_box(box_idx, grid_idx=0):
    a, b = cvt_box_to_grid_pos(box_idx)
    for i in range(a, a+root_N):
        for j in range(b, b+root_N):
            if grids[grid_idx][i][j] != 0:
                return False
    return True

#This function checks if the given box is divided into empty cells and non-empty cells or not
def is_mix_box(box_idx, grid_idx=0):
    empty_cells = 0
    a, b = cvt_box_to_grid_pos(box_idx)
    for i in range(a, a+root_N):
        for j in range(b, b+root_N):
            if grids[grid_idx][i][j] == 0:
                empty_cells += 1
    return empty_cells == (N+1) // 2

#This function copies the all boxes of the given grid in the shared boxes in the other grids
def cpy_similar_boxes(grid_idx):
    for i in range(0, N, root_N):
        for j in range(0, N, root_N):
            box_idx = cvt_grid_pos_to_box(i, j)
            similar_boxes = get_similar_boxes(box_idx, grid_idx)
            cpy_box_in_shared_boxes(box_idx, similar_boxes, grid_idx, True)

#This function generates cells in the grids
def generate_cells(grid_idx=0):
    for k in range(0, N, root_N):
        box_idx = cvt_grid_pos_to_box(k, k)
        if not is_empty_box(box_idx, grid_idx):
            continue
        for i in range(root_N):
            for j in range(root_N):
                n = random.randint(1, N)
                while not check_valid_value_in_shared_boxes(k+i, k+j, n, grid_idx) or \
                      check_original_cell(k+i, k+j, grid_idx):
                    n = random.randint(1, N)
                grids[grid_idx][k+i][k+j] = n
                cpy_grids[grid_idx][k+i][k+j] = n

#This function removes cells in the grids
def remove_cells(grid_idx=0):
    for k in range((N+1)//2):
        for i in range(0, N, root_N):
            for j in range(0, N, root_N):
                box_idx = cvt_grid_pos_to_box(i, j)
                if is_mix_box(box_idx, grid_idx):
                    continue
                t1 = random.randint(0, root_N-1)
                t2 = random.randint(0, root_N-1)
                while not check_original_cell(i+t1, j+t2, grid_idx):
                    t1 = random.randint(0, root_N-1)
                    t2 = random.randint(0, root_N-1)
                grids[grid_idx][i+t1][j+t2] = 0
                cpy_grids[grid_idx][i+t1][j+t2] = 0

#This function generates cells in the given grid
def generate_grids():
    #Generate cells in the grid
    generate_cells(0)    
    for grid_idx in range(n_grids[mode]):
        #Solve the complete grid
        solve_grid(0, 0, grid_idx)
        #Copy the similar boxes in the another grids
        cpy_similar_boxes(grid_idx)
    for grid_idx in range(n_grids[mode]):
        #Remove cells in the grid to be solved
        remove_cells(grid_idx)
        #Copy the similar boxes in the another grids
        cpy_similar_boxes(grid_idx)

#This function clears the game structures
def grid_clear():
	global grids, cpy_grids
	grids = [[[0] * N for j in range(N)] for i in range(n_grids[mode])]
	cpy_grids = [[[0] * N for j in range(N)] for i in range(n_grids[mode])]

#This function reads a valid position and value inputs
def read_input():
    grid_idx, i, j, v = map(int, input('Enter the row index and column index and value: ').split())
    while not check_valid_grid_index(grid_idx) or not check_valid_position(i, j) or \
          not check_valid_value_in_shared_boxes(i, j, v, grid_idx) or check_original_cell(i, j, grid_idx):
        grid_idx, i, j, v = map(int, input('Enter a valid row index and column index and value: ').split())
    return grid_idx, i, j, v


#MAIN FUNCTION
def play_game():
    print("Multi-Sudoku Game!")
    print("Welcome...")
    print("============================")
    while True:
        #Prints the grids
        print_grids()
        #Read an input from the player
        grid_idx, i, j, v = read_input()
        #Set the input position with the value
        set_cell(i, j, v, grid_idx)
        #Check if the grid has a win state
        if check_win():
            #Prints the grids
            print_grids()
            #Announcement of the final statement
            print('Congrats, You won!')
            break

while True:
    set_config()
    grid_clear()
    generate_grids()
    play_game()
    c = input('Play Again [Y/N] ')
    if c not in 'yY':
        break
