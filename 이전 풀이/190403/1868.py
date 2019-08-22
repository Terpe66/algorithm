import sys
sys.stdin = open("1868.txt")

from collections import deque

for T in range(int(input())):
    size = int(input())
    board = [list(map(str, input())) for _ in range(size)]

    drow = [-1, -1, 0, 1, 1, 1, 0, -1]
    dcol = [0, 1, 1, 1, 0, -1, -1, -1]

    Q = deque()
    for row in range(size):
        for col in range(size):
            if board[row][col] == ".":
                for idx in range(8):
                    nrow, ncol = row + drow[idx], col + dcol[idx]
                    if 0 <= nrow < size and 0 <= ncol < size and board[nrow][ncol] == "*":
                        break
                else:
                    board[row][col] = "0"
                    Q.append((row, col))
                    tmp = deque()
                    while Q:
                        r, c = Q.popleft()
                        mchk = True
                        for idx in range(8):
                            nrow, ncol = r + drow[idx], c + dcol[idx]
                            if 0 <= nrow < size and 0 <= ncol < size:
                                if board[nrow][ncol] == "*":
                                    mchk = False
                                if board[nrow][ncol] == ".":
                                    tmp.append((nrow, ncol))
                        if mchk:
                            if board[r][c] == "1":
                                board[r][c] = "2"
                            while tmp:
                                i, j = tmp.popleft()
                                if board[i][j] == ".":
                                    board[i][j] = "1"
                                Q.append((i, j))
                        else:
                            board[r][c] = "1"
                            tmp.clear()

    ans = 0
    for row in range(size):
        for col in range(size):
            if board[row][col] == "0" or board[row][col] == ".":
                ans += 1

    print(f"#{T + 1} {ans}")
