ROW_SIZE = 9
SMALL = 3

def init_board():
    row = [0] * (ROW_SIZE)
    board = []
    for i in range(ROW_SIZE):
        board.append(row[:])
    return board

def legal_placement(board, col, row):
    current = board[col][row]
    for i in range(ROW_SIZE):
        if i == col: continue
        if board[i][row] == current:
            return False
    for i in range(ROW_SIZE):
        if i == row: continue
        if board[col][i] == current:
            return False
    factor_x = col // SMALL
    factor_y = row // SMALL
    for x in range(SMALL):
        for y in range(SMALL):
            if x == col and y == row: continue
            if board[x + factor_x][y + factor_y] == current:
                return False
    return True

def print_board(board, filename):
    SEP = ','
    with open(filename, 'w') as f:
        for j in range(ROW_SIZE):
            for i in range(ROW_SIZE):
                txt = str(board[i][j]) if i == 0 else SEP + str(board[i][j])
                f.write(txt)
            if j != 8: f.write('\n')
        f.close()

FILENAME = 'SUDOKU_SOL.txt'
def play_game(board):
    if play_game_helper(board, 0, 0):
        print_board(board, FILENAME)
    else:
        print("There's no solution for this board")

def play_game_helper(board, c, r):
    board = board[:]
    row = r + c // 9
    col = c % 9
    if row >= 9: return True
    if board[col][row] == 0:
        for i in range(1, ROW_SIZE + 1):
            board[col][row] = i
            if legal_placement(board, col, row):
                if play_game_helper(board, col + 1, row): return True
        return False
    else:
        if legal_placement(board, col, row):
            return play_game_helper(board, col + 1, row)
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
        legal_col = col <= 9 and col >= 1
        legal_row = row <= 9 and row >= 1
        legal_num = num <= 9 and num >= 1
        return legal_col and legal_row and legal_num
        
    board = init_board()
    inpt = ''
    print('Enter values, type "end" when finished.')
    while inpt != 'end':
        inpt = input('col,row num: ')
        if legal_input(inpt):
            col = int(inpt[:1]) - 1
            row = int(inpt[2:3]) - 1
            num = inpt[4:]
            board[col][row] = num
        else:
            if inpt == 'end': break
            print('Illegal input, try again')
    return board
