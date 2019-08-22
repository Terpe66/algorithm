import sys
sys.stdin = open("01.txt")

for t in range(int(input())):
    size, X = map(int, input().split())

    board = []
    for _ in range(size):
        board.append(list(map(int, input().split())))

    row, col, ans = 0, 0, 300
    while row + X - 1 < size:
        while col + X - 1 < size:
            ridx, cidx, lft, rgt = row, col, 0, 0
            while ridx < row + X and cidx < col + X:
                lft += board[ridx][cidx]
                ridx += 1
                cidx += 1

            ridx, cidx = row, col + X - 1
            while ridx < row + X and cidx >= 0:
                rgt += board[ridx][cidx]
                ridx += 1
                cidx -= 1

            new = abs(rgt - lft)
            if new < ans:
                ans = new
            col += 1
        row += 1
        col = 0

    print("#{} {}".format(t+1, ans))