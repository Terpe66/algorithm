import sys
sys.stdin = open("14502.txt")


def reset():
    for i in range(len(zeros)):
        row, col = zeros[i]
        if visit[i] == False:
            board[row][col] = 0


def check_zeros():
    point = 0
    for row, col in zeros:
        if board[row][col] == 0:
            point += 1

    return point


def check_virus(row, col):

    for i in range(4):
        nRow, nCol = row + dir[i], col + dir[3 - i]
        if 0 <= nRow < height and 0 <= nCol < width and board[nRow][nCol] == 0:
            board[nRow][nCol] = 2
            check_virus(nRow, nCol)


def set_wall(idx, wall):
    global answer

    if wall == 3:
        for row, col in virus:
            check_virus(row, col)

        new = check_zeros()
        if answer < new:
            answer = new
        reset()

        return

    for i in range(idx, len(zeros)):
        row, col = zeros[i]
        if board[row][col] == 0:
            board[row][col] = 1
            visit[i] = True
            set_wall(i + 1, wall + 1)
            visit[i] = False
            board[row][col] = 0


dir = [1, -1, 0, 0]

for T in range(int(input())):
    answer = 0
    height, width = map(int, input().split())
    board = []
    zeros = []
    virus = []

    for row in range(height):
        inputs = list(map(int, input().split()))
        for col in range(width):
            if inputs[col] == 2:
                virus.append((row, col))
            elif inputs[col] == 0:
                zeros.append((row, col))
        board.append(inputs)

    visit = [False] * len(zeros)

    set_wall(0, 0)

    print(answer)