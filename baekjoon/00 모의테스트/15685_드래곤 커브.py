import sys
sys.stdin = open("15685.txt")


def curve():
    point = 0
    for i in range(100):
        for j in range(100):
            if 1 == board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]:
                point += 1

    return point


def dragon(col, row, dir, gene):
    draw = 2 ** gene
    temp = [(col, row)]

    if dir == 0:
        temp.append((col + 1, row))
    elif dir == 1:
        temp.append((col, row - 1))
    elif dir == 2:
        temp.append((col - 1, row))
    elif dir == 3:
        temp.append((col, row + 1))
    draw -= 1

    while draw > 0:
        c, r = temp[-1]
        for i in range(len(temp) - 2, -1, -1):
            nc, nr = temp[i]
            tr, tc = r - (c - nc), c + (r - nr)
            temp.append((tc, tr))
            draw -= 1

    for i in range(len(temp)):
        c, r = temp[i]
        board[r][c] = 1


for T in range(int(input())):
    board = [[0] * 101 for _ in range(101)]
    for i in range(int(input())):
        x, y, d, g = map(int, input().split())
        dragon(x, y, d, g)

    answer = curve()
    print(answer)