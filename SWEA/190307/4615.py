import sys
sys.stdin = open("4615.txt")

for tc in range(int(input())):
    size, turn = map(int, input().split())

    board = [[0]*size for _ in range(size)]
    T = []

    for _ in range(turn):
        r, c, s = map(int, input().split())
        r -= 1
        c -= 1
        T.append((r, c, s))

    board[size//2][size//2] = 2
    board[size//2-1][size//2] = 1
    board[size//2][size//2-1] = 1
    board[size//2-1][size//2-1] = 2

    O = (2, 1, 2)

    for X in T:
        col, row, S = X[0], X[1], X[2]
        if not board[row][col]:
            board[row][col] = S

            while row > 0 and board[row-1][col] == O[S-1]:
                row -= 1
            if row > 0 and board[row-1][col] == O[S]:
                while row < X[1]:
                    board[row][col] = S
                    row += 1

            col, row = X[0], X[1]
            while row < size-1 and board[row+1][col] == O[S-1]:
                row += 1
            if row < size-1 and board[row+1][col] == O[S]:
                while row > X[1]:
                    board[row][col] = S
                    row -= 1

            col, row = X[0], X[1]
            while col > 0 and board[row][col-1] == O[S-1]:
                col -= 1
            if col > 0 and board[row][col-1] == O[S]:
                while col < X[0]:
                    board[row][col] = S
                    col += 1

            col, row = X[0], X[1]
            while col < size-1 and board[row][col+1] == O[S-1]:
                col += 1
            if col < size-1 and board[row][col+1] == O[S]:
                while col > X[0]:
                    board[row][col] = S
                    col -= 1

            col, row = X[0], X[1]
            while row > 0 and col > 0 and board[row-1][col-1] == O[S-1]:
                col -= 1
                row -= 1
            if row > 0 and col > 0 and board[row-1][col-1] == O[S]:
                while row < X[1] and col < X[0]:
                    board[row][col] = S
                    col += 1
                    row += 1

            col, row = X[0], X[1]
            while row < size-1 and col < size-1 and board[row+1][col+1] == O[S-1]:
                col += 1
                row += 1
            if row < size-1 and col < size-1 and board[row+1][col+1] == O[S]:
                while row > X[1] and col > X[0]:
                    board[row][col] = S
                    col -= 1
                    row -= 1

            col, row = X[0], X[1]
            while row < size-1 and col > 0 and board[row+1][col-1] == O[S-1]:
                col -= 1
                row += 1
            if row < size - 1 and col > 0 and board[row+1][col-1] == O[S]:
                while row > X[1] and col < X[0]:
                    board[row][col] = S
                    col += 1
                    row -= 1

            col, row = X[0], X[1]
            while row > 0 and col < size-1 and board[row-1][col+1] == O[S-1]:
                col += 1
                row -= 1
            if row > 0 and col < size-1 and board[row-1][col+1] == O[S]:
                while row < X[1] and col > X[0]:
                    board[row][col] = S
                    col -= 1
                    row += 1

    black, white = 0, 0
    for row in range(size):
        for col in range(size):
            if board[row][col] == 1:
                black += 1
            elif board[row][col] == 2:
                white += 1

    print(f"#{tc+1} {black} {white}")
