import sys
sys.stdin = open("15684.txt")


def count_stick():

    for col in range(width):
        c = col
        for row in range(stick):
            if board[row][c] == 1:
                c -= 1
            elif c + 1 < width and board[row][c + 1] == 1:
                c += 1
        if col != c:
            return False
    return True


def let_stick(row, col, stk, until):

    if stk == until:
        return count_stick()

    r = row
    for c in range(col, width - 1):
        while r < stick:
            if c + 2 < width and board[r][c + 2] == 1:
                r += 1
                continue

            if board[r][c] == 0 and board[r][c + 1] == 0:
                board[r][c + 1] = 1
                if let_stick(r + 1, c, stk + 1, until):
                    return True
                board[r][c + 1] = 0
            r += 1
        r = 0


for T in range(int(input())):
    width, height, stick = map(int, input().split())
    board = [[0] * width for _ in range(stick)]

    if height == 0:
        answer = 0
    else:
        for i in range(height):
            row, col = map(int, input().split())
            board[row - 1][col] = 1

        for i in range(4):
            if let_stick(0, 0, 0, i):
                answer = i
                break
        else:
            answer = -1

    print(answer)






