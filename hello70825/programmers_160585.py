def solution(board):
    o_num, x_num = 0, 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O': o_num += 1
            if board[i][j] == 'X': x_num += 1
    if x_num > o_num: return 0
    if not (o_num == x_num or o_num - 1 == x_num): return 0

    o_win_flag, x_win_flag = False, False
    for i in range(3):
        horizontal = ''
        vertical = ''
        for j in range(3):
            horizontal += board[i][j]
            vertical += board[j][i]
        if "OOO" in [horizontal, vertical]: o_win_flag = True
        if "XXX" in [horizontal, vertical]: x_win_flag = True
    if board[0][0] + board[1][1] + board[2][2] == "OOO": o_win_flag = True
    if board[0][2] + board[1][1] + board[2][0] == "OOO": o_win_flag = True
    if board[0][0] + board[1][1] + board[2][2] == "XXX": x_win_flag = True
    if board[0][2] + board[1][1] + board[2][0] == "XXX": x_win_flag = True
    if o_win_flag and x_win_flag: return 0
    if o_win_flag and o_num - 1 != x_num: return 0
    if x_win_flag and o_num != x_num: return 0

    return 1