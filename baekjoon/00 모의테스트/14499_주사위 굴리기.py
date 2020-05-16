import sys
sys.stdin = open("14499.txt")

for T in range(int(input())):
    dice = [[None, 0, None, None], [0, 0, 0, 0], [None, 0, None, None], [None, 0, None, None]]
    dRow, dCol = 1, 1
    height, width, row, col, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(height)]
    go = list(map(int, input().split()))

    for i in range(k):
        bRow, bCol = dRow, dCol
        chk = False
        if go[i] == 1:
            col += 1
            if col == width:
                col -= 1
                chk= True
            else:
                dCol -= 1
                if dCol == -1:
                    dCol = 3
        elif go[i] == 2:
            col -= 1
            if col == -1:
                col += 1
                chk = True
            else:
                dCol += 1
                if dCol == 4:
                    dCol = 0
        elif go[i] == 3:
            row -= 1
            if row == -1:
                row += 1
                chk = True
            else:
                dRow += 1
                if dRow == 4:
                    dRow = 0
        elif go[i] == 4:
            row += 1
            if row == height:
                row -= 1
                chk = True
            else:
                dRow -= 1
                if dRow == -1:
                    dRow = 3

        if chk:
            continue

        if dRow != bRow:
            for c in range(4):
                if c != dCol:
                    dice[bRow][c], dice[dRow][c] = dice[dRow][c], dice[bRow][c]
        else:
            for r in range(4):
                if r != dRow:
                    dice[r][dCol], dice[r][bCol] = dice[r][bCol], dice[r][dCol]

        cnt = 2
        nRow, nCol = dRow, dCol
        while cnt > 0:
            cnt -= 1
            nRow += 1
            if nRow == 4:
                nRow = 0
        cnt = 2
        nnRow, nnCol = dRow, dCol
        while cnt > 0:
            cnt -= 1
            nnCol += 1
            if nnCol == 4:
                nnCol = 0

        if board[row][col] == 0:
            if go[i] < 3:
                board[row][col] = dice[nnRow][nnCol]
            else:
                board[row][col] = dice[nRow][nCol]
            dice[nRow][nCol] = board[row][col]
            dice[nnRow][nnCol] = board[row][col]
        else:
            dice[nRow][nCol] = board[row][col]
            dice[nnRow][nnCol] = board[row][col]
            board[row][col] = 0

        print(dice[dRow][dCol])
    print("#####")
