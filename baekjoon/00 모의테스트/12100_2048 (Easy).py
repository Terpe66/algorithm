import copy
import sys
sys.stdin = open("12100.txt")


def rotate(board):
    temp = [[0] * length for _ in range(length)]

    for i in range(length):
        for j in range(length):
            temp[j][i] = board[length - i - 1][j]

    for i in range(length):
        for j in range(length):
            board[i][j] = temp[i][j]


def get_max(board):
    now = 0

    for i in range(length):
        for j in range(length):
            if now < board[i][j]:
                now = board[i][j]

    return now


def up(board):
    temp = [[0] * length for _ in range(length)]

    for j in range(length):
        updated = 0
        target = -1
        for i in range(length):
            if board[i][j] == 0:
                continue

            if updated == 1 and board[i][j] == temp[target][j]:
                temp[target][j] *= 2
                updated = 0
            else:
                target += 1
                temp[target][j] = board[i][j]
                updated = 1
        for t in range(target + 1, length):
            temp[t][j] = 0

    for i in range(length):
        for j in range(length):
            board[i][j] = temp[i][j]


def dfs(board, cnt):
    global answer

    if cnt == 5:
        now = get_max(board)
        if answer < now:
            answer = now
        return

    for i in range(4):
        new = copy.deepcopy(board)
        up(new)
        dfs(new[:], cnt + 1)
        rotate(board)


answer = 0
length = int(input())
MAP = [list(map(int, input().split())) for _ in range(length)]

dfs(MAP, 0)

print(answer)