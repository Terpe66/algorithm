from collections import deque
import sys
sys.stdin = open("13460.txt")


for T in range(int(input())):
    answer = -1
    height, width = map(int, input().split())
    board = []
    rb = [0, 0, 0, 0, 0]
    for i in range(height):
        inputs = input()
        if 0 < i < height - 1:
            for j in range(width):
                if inputs[j] == '.':
                    continue
                if inputs[j] == 'R':
                    rb[:2] = [i, j]
                elif inputs[j] == 'B':
                    rb[2:4] = [i, j]
                elif inputs[j] == 'O':
                    hole = (i, j)
        board.append(inputs)

    di = [1, -1, 0, 0]
    visitRB = [[[[False] * 10 for i in range(10)] for o in range(10)] for p in range(10)]
    visitRB[rb[0]][rb[1]][rb[2]][rb[3]] = True
    move = deque()
    move.append(rb)
    while move:
        rRow, rCol, bRow, bCol, cnt = move.popleft()

        if cnt > 10:
            continue

        if board[rRow][rCol] == 'O' and board[bRow][bCol] != 'O':
            answer = cnt
            break

        for i in range(4):
            nRow, nCol = rRow, rCol
            nbRow, nbCol = bRow, bCol

            while True:
                if board[nRow][nCol] != '#' and board[nRow][nCol] != 'O':
                    nRow += di[i]
                    nCol += di[3 - i]
                else:
                    if board[nRow][nCol] == '#':
                        nRow -= di[i]
                        nCol -= di[3 - i]
                    break

            while True:
                if board[nbRow][nbCol] != '#' and board[nbRow][nbCol] != 'O':
                    nbRow += di[i]
                    nbCol += di[3 - i]
                else:
                    if board[nbRow][nbCol] == '#':
                        nbRow -= di[i]
                        nbCol -= di[3 - i]
                    break

            if nRow == nbRow and nCol == nbCol:
                if board[nRow][nCol] != 'O':
                    rDist = abs(rRow - nRow) + abs(rCol - nCol)
                    bDist = abs(bRow - nbRow) + abs(bCol - nbCol)
                    if rDist > bDist:
                        nRow -= di[i]
                        nCol -= di[3 - i]
                    else:
                        nbRow -= di[i]
                        nbCol -= di[3 - i]

            if visitRB[nRow][nCol][nbRow][nbCol] == False:
                visitRB[nRow][nCol][nbRow][nbCol] = True
                move.append((nRow, nCol, nbRow, nbCol, cnt + 1))

    print(answer)