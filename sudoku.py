ROW_SIZE = 9
SMALL = 3

def init_board():
    row = [0] * (ROW_SIZE)
    board = []
    for i in range(ROW_SIZE):
        board.append(row[:])
    return board

def legal_placement(board, col, row):
    current = board[row][col]
    for c in range(ROW_SIZE):
        if c == col: continue
        if board[row][c] == current:
            return False
    for r in range(ROW_SIZE):
        if r == row: continue
        if board[r][col] == current:
            return False
    factor_y = (col // SMALL) * SMALL
    factor_x = (row // SMALL) * SMALL
    for x in range(SMALL):
        for y in range(SMALL):
            if x + factor_x == row and y + factor_y == col: continue
            if board[x + factor_x][y + factor_y] == current:
                return False
    return True

def print_board(board, filename):
    SEP = '\t'
    with open(filename, 'w') as f:
        for row in range(ROW_SIZE):
            for col in range(ROW_SIZE):
                txt = str(board[row][col]) if col == 0 else SEP + str(board[row][col])
                f.write(txt)
            if row != ROW_SIZE - 1: f.write('\n' + '\n')
        f.close()

FILENAME = 'SUDOKU_SOL.txt'
def play_game(board):
    if play_game_helper(board, 0, 0):
        print_board(board, FILENAME)
    else:
        print("There's no solution for this board")

def play_game_helper(board, c, r):
    new_board = [row[:] for row in board]
    row = r + c // ROW_SIZE
    col = c % ROW_SIZE
    if row >= ROW_SIZE: return True
    if new_board[row][col] == 0:
        for i in range(1, ROW_SIZE + 1):
            new_board[row][col] = i
            if legal_placement(new_board, col, row):
                if play_game_helper(new_board, col + 1, row):
                    return True
        return False
    else:
        if legal_placement(new_board, col, row):
            return play_game_helper(new_board, col + 1, row)
        else:
            return False

def set_new_board():

    def legal_input(txt):
        if not ',' in txt: return False
        col = txt[:1]
        row = txt[2:3]
        num = txt[4:]
        numbers = col.isnumeric() and row.isnumeric() and num.isnumeric()
        if not numbers: return False
        col = int(col)
        row = int(row)
        num = int(num)
        legal_col = col <= ROW_SIZE and col >= 1
        legal_row = row <= ROW_SIZE and row >= 1
        legal_num = num <= ROW_SIZE and num >= 1
        return legal_col and legal_row and legal_num
        
    board = init_board()
    inpt = ''
    print('Enter values, type "end" when finished.')
    while inpt != 'end':
        inpt = input('row,col num: ')
        if legal_input(inpt):
            row = int(inpt[:1]) - 1
            col = int(inpt[2:3]) - 1
            num = inpt[4:]
            board[row][col] = num
        else:
            if inpt == 'end': break
            print('Illegal input, try again')
    return board
