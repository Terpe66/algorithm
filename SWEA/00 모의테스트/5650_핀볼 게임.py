import sys
sys.stdin = open("5650.txt")


def change(r, c, d, n):
    if n < 6:
        nr, nc, nd, chk = r, c, change_list[n - 1][d], True
    else:
        nr, nc = worm[now - 6][0]
        if nr == r and nc == c:
            nr, nc = worm[now - 6][1]
        nd, chk = d, False
    return nr, nc, nd, chk


change_list = [[2, 3, 1, 0], [1, 3, 0, 2], [3, 2, 0, 1], [2, 0, 3, 1], [2, 3, 0, 1]]
drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for T in range(int(input())):
    answer = 0
    length = int(input())
    board = [[5] * (length + 2) for _ in range(length + 2)]
    worm = [[] for _ in range(5)]
    for i in range(length):
        inputs = list(map(int, input().split()))
        for j in range(length):
            board[i + 1][j + 1] = inputs[j]
            if inputs[j] >= 6:
                worm[inputs[j] - 6].append((i + 1, j + 1))

    for row in range(1, length + 1):
        for col in range(1, length + 1):
            if board[row][col] == 0:
                # print(row, col)
                for i in range(4):
                    d = i
                    nrow, ncol = row, col
                    point = 0
                    while True:
                        nrow, ncol = nrow + drc[d][0], ncol + drc[d][1]
                        now = board[nrow][ncol]
                        if now == -1:
                            break

                        if now:
                            nrow, ncol, d, check = change(nrow, ncol, d, now)
                            if check:
                                point += 1

                        if row == nrow and col == ncol:
                            break

                    answer = max(answer, point)

    print("#{} {}".format(T + 1, answer))
