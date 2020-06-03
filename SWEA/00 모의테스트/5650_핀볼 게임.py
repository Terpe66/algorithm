import sys
sys.stdin = open("5650.txt")


def find_worm(r, c, d):

    idx = board[r][c] - 6
    nr, nc = worm[idx][0]
    if r == nr and c == nc:
        nr, nc = worm[idx][1]

    if d == 0:
        nr -= 1
    elif d == 1:
        nc += 1
    elif d == 2:
        nr += 1
    elif d == 3:
        nc -= 1

    return nr, nc, d + 4


def ball(r, c, dir):

    if dir == 0:
        for i in range(r, -1, -1):
            if i == row and c == col:
                return i, c, 4
            elif board[i][c] == -1:
                return i, c, -1
            elif board[i][c] in (1, 4, 5):
                return i + 1, c, 2
            elif board[i][c] == 2:
                return i, c + 1, 1
            elif board[i][c] == 3:
                return i, c - 1, 3
            elif board[i][c] > 5:
                return find_worm(i, c, dir)
        else:
            return 0, c, 2
    elif dir == 1:
        for i in range(c, length):
            if r == row and i == col:
                return r, i, 4
            elif board[r][i] == -1:
                return r, i, -1
            elif board[r][i] in (1, 2, 5):
                return r, i - 1, 3
            elif board[r][i] == 3:
                return r + 1, i, 2
            elif board[r][i] == 4:
                return r - 1, i, 0
            elif board[r][i] > 5:
                return find_worm(r, i, dir)
        else:
            return r, length - 1, 3
    elif dir == 2:
        for i in range(r, length):
            if i == row and c == col:
                return i, c, 4
            elif board[i][c] == -1:
                return i, c, -1
            elif board[i][c] in (2, 3, 5):
                return i - 1, c, 0
            elif board[i][c] == 1:
                return i, c + 1, 1
            elif board[i][c] == 4:
                return i, c - 1, 3
            elif board[i][c] > 5:
                return find_worm(i, c, dir)
        else:
            return length - 1, c, 0
    elif dir == 3:
        for i in range(c, -1, -1):
            if r == row and i == col:
                return r, i, 4
            elif board[r][i] == -1:
                return r, i, -1
            elif board[r][i] in (3, 4, 5):
                return r, i + 1, 1
            elif board[r][i] == 1:
                return r - 1, i, 0
            elif board[r][i] == 2:
                return r + 1, i, 2
            elif board[r][i] > 5:
                return find_worm(r, i, dir)
        else:
            return r, 0, 1


def go(r, c, dir):
    point = 0

    d = dir
    nr, nc = r, c
    while True:
        ret = ball(nr, nc, d)
        if ret[2] == -1:
            return point
        else:
            nr, nc, d = ret
            if d > 3:
                d -= 4
            else:
                point += 1
        if nr == row and nc == col:
            return point


for T in range(int(input())):
    answer = 0
    length = int(input())
    board = [[0] * length for _ in range(length)]
    worm = [[] for _ in range(5)]
    for i in range(length):
        inputs = list(map(int, input().split()))
        for j in range(length):
            board[i][j] = inputs[j]
            if inputs[j] >= 6:
                worm[inputs[j] - 6].append((i, j))

    for row in range(length):
        for col in range(length):
            if board[row][col] == 0:
                answer = max(answer, go(row - 1, col, 0))
                answer = max(answer, go(row, col + 1, 1))
                answer = max(answer, go(row + 1, col, 2))
                answer = max(answer, go(row, col - 1, 3))

    print("#{} {}".format(T + 1, answer))
