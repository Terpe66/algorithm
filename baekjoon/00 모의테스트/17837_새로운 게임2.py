import sys
sys.stdin = open("17837.txt")


def detail_move(i, nr, nc, nk):
    horse_board[i] = (nr, nc, nk)


def move_horse(idx):
    row, col, rank = horse_board[idx]
    dir = board[row][col][1][rank][1]

    if dir == 1:
        r, c = row, col + 1
    elif dir == 2:
        r, c = row, col - 1
    elif dir == 3:
        r, c = row - 1, col
    elif dir == 4:
        r, c = row + 1, col

    if 0 <= r < length and 0 <= c < length and board[r][c][0] != 2:
        if board[r][c][0] == 0:
            for i in range(rank, len(board[row][col][1])):
                ni, nd, nr = board[row][col][1].pop(rank)
                board[r][c][1].append((ni, nd, len(board[r][c][1])))
                detail_move(ni, r, c, len(board[r][c][1]) - 1)

        elif board[r][c][0] == 1:
            for i in range(rank, len(board[row][col][1])):
                ni, nd, nr = board[row][col][1].pop()
                board[r][c][1].append((ni, nd, len(board[r][c][1])))
                detail_move(ni, r, c, len(board[r][c][1]) - 1)

    elif -1 == c or c == length or -1 == r or r == length or board[r][c][0] == 2:
        if dir == 1:
            c -= 2
        elif dir == 2:
            c += 2
        elif dir == 3:
            r += 2
        elif dir == 4:
            r -= 2

        if 0 <= r < length and 0 <= c < length and board[r][c][0] != 2:
            ti, td, tr = board[row][col][1].pop(rank)
            if dir == 1:
                td = 2
            elif dir == 2:
                td = 1
            elif dir == 3:
                td = 4
            elif dir == 4:
                td = 3
            if board[r][c][0] == 0:
                board[r][c][1].append((ti, td, len(board[r][c][1])))
                detail_move(ti, r, c, len(board[r][c][1]) - 1)
                for i in range(rank, len(board[row][col][1])):
                    ni, nd, nr = board[row][col][1].pop(rank)
                    board[r][c][1].append((ni, nd, len(board[r][c][1])))
                    detail_move(ni, r, c, len(board[r][c][1]) - 1)
            elif board[r][c][0] == 1:
                for i in range(rank, len(board[row][col][1])):
                    ni, nd, nr = board[row][col][1].pop()
                    board[r][c][1].append((ni, nd, len(board[r][c][1])))
                    detail_move(ni, r, c, len(board[r][c][1]) - 1)
                board[r][c][1].append((ti, td, len(board[r][c][1])))
                detail_move(ti, r, c, len(board[r][c][1]) - 1)
        else:
            ti, td, tr = board[row][col][1][rank]
            if dir == 1:
                td = 2
            elif dir == 2:
                td = 1
            elif dir == 3:
                td = 4
            elif dir == 4:
                td = 3
            board[row][col][1][rank] = (ti, td, tr)


def check_four():
    check_dict = {}
    for i in range(horse):
        r, c, k = horse_board[i]
        if check_dict.get((r, c), False):
            check_dict[(r, c)] += 1
        else:
            check_dict[(r, c)] = 1
        if check_dict[(r, c)] > 3:
            return True

    return False


for T in range(int(input())):
    length, horse = map(int, input().split())
    board = [[[0, []] for _ in range(length)] for _ in range(length)]
    horse_board = []

    for r in range(length):
        inputs = list(map(int, input().split()))
        for c in range(length):
            board[r][c][0] = inputs[c]

    for i in range(horse):
        r, c, d = map(int, input().split())
        board[r - 1][c - 1][1].append((i, d, 0))
        horse_board.append((r - 1, c - 1, 0))

    t = 0
    check = True
    while check:
        t += 1
        for i in range(horse):
            move_horse(i)
            if check_four():
                check = False
                break

        if t > 1000:
            t = -1
            break

    print(t)
