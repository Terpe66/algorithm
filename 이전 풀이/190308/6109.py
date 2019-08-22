import sys
sys.stdin = open("6109.txt")

for t in range(int(input())):
    N, dlru = input().split()
    N = int(N)

    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    if dlru == "up":
        row, col = 0, 0
        while col < N:
            while row < N:
                while row < N and not board[row][col]:
                    row += 1

                ridx = row+1
                while ridx < N and not board[ridx][col]:
                    ridx += 1

                if row >= N or ridx >= N:
                    row, ridx = 0, 1
                    while row < N and ridx < N:
                        if not board[row][col]:
                            while ridx < N and not board[ridx][col]:
                                ridx += 1
                            if ridx < N:
                                board[row][col], board[ridx][col] = board[ridx][col], 0
                        row += 1
                        ridx += 1
                    break

                if board[row][col] == board[ridx][col]:
                    board[row][col] *= 2
                    board[ridx][col] = 0
                row = ridx
            row = 0
            col += 1

    if dlru == "down":
        row, col = N-1, 0
        while col < N:
            while row >= 0:
                while row >= 0 and not board[row][col]:
                    row -= 1

                ridx = row - 1
                while ridx >= 0 and not board[ridx][col]:
                    ridx -= 1

                if row < 0 or ridx < 0:
                    row, ridx = N-1, N-2
                    while row >= 0 and ridx >= 0:
                        if not board[row][col]:
                            while ridx >= 0 and not board[ridx][col]:
                                ridx -= 1
                            if ridx >= 0:
                                board[row][col], board[ridx][col] = board[ridx][col], 0
                        row -= 1
                        ridx = ridx - 1
                    break

                if board[row][col] == board[ridx][col]:
                    board[row][col] *= 2
                    board[ridx][col] = 0
                row = ridx
            row = N-1
            col += 1

    if dlru == "left":
        row, col = 0, 0
        while row < N:
            while col < N:
                while col < N and not board[row][col]:
                    col += 1

                cidx = col + 1
                while cidx < N and not board[row][cidx]:
                    cidx += 1

                if col >= N or cidx >= N:
                    col, cidx = 0, 1
                    while col < N and cidx < N:
                        if not board[row][col]:
                            while cidx < N and not board[row][cidx]:
                                cidx += 1
                            if cidx < N:
                                board[row][col], board[row][cidx] = board[row][cidx], 0
                        col += 1
                        cidx = cidx + 1
                    break

                if board[row][col] == board[row][cidx]:
                    board[row][col] *= 2
                    board[row][cidx] = 0
                col = cidx
            col = 0
            row += 1

    if dlru == "right":
        row, col = 0, N-1
        while row < N:
            while col >= 0:
                while col >= 0 and not board[row][col]:
                    col -= 1

                cidx = col - 1
                while cidx >= 0 and not board[row][cidx]:
                    cidx -= 1

                if col < 0 or cidx < 0:
                    col, cidx = N-1, N-2
                    while col >= 0 and cidx >= 0:
                        if not board[row][col]:
                            while cidx >= 0 and not board[row][cidx]:
                                cidx -= 1
                            if cidx >= 0:
                                board[row][col], board[row][cidx] = board[row][cidx], 0
                        col -= 1
                        cidx = cidx - 1
                    break

                if board[row][col] == board[row][cidx]:
                    board[row][col] *= 2
                    board[row][cidx] = 0
                col = cidx
            row += 1
            col = N-1

    print(f"#{t+1}")
    for line in board:
        for l in line:
            print(l, end=" ")
        print()