import sys
sys.stdin = open("14890.txt")

for T in range(int(input())):
    answer = 0
    length, bridge = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(length)]
    bridgeCheck = [[0] * length for _ in range(length)]

    for row in range(length):
        col = 0
        rChk = True
        while col + 1 < length:
            if board[row][col] > board[row][col + 1] and col + bridge >= length:
                rChk = False
                break
            if board[row][col] < board[row][col + 1] and col + 1 - bridge < 0:
                rChk = False
                break
            comp = abs(board[row][col] - board[row][col + 1])
            if comp > 1:
                rChk = False
                break
            if comp == 1:
                bChk = True
                if board[row][col] > board[row][col + 1]:
                    nCol = col + 1
                    while nCol < col + bridge:
                        if board[row][nCol] != board[row][nCol + 1] or bridgeCheck[row][nCol] == 1 or bridgeCheck[row][nCol + 1] == 1:
                            bChk = False
                            break
                        nCol += 1
                    if bChk:
                        for c in range(col + 1, col + bridge + 1):
                            bridgeCheck[row][c] = 1
                        col = nCol
                    else:
                        rChk = False
                        break
                elif board[row][col] < board[row][col + 1]:
                    if bridge == 1:
                        if bridgeCheck[row][col] == 1:
                            rChk = False
                            break
                    nCol = col
                    while nCol > col + 1 - bridge:
                        if board[row][nCol] != board[row][nCol - 1] or bridgeCheck[row][nCol] == 1 or bridgeCheck[row][nCol - 1] == 1:
                            bChk = False
                            break
                        nCol -= 1
                    if bChk:
                        for c in range(col + 1 - bridge, col + 1):
                            bridgeCheck[row][c] = 1
                        col += 1
                    else:
                        rChk = False
                        break
            if comp == 0:
                col += 1
        if rChk:
            answer += 1

    for col in range(length):
        row = 0
        dChk = True
        while row + 1 < length:
            if board[row][col] > board[row + 1][col] and row + bridge >= length:
                dChk = False
                break
            if board[row][col] < board[row + 1][col] and row + 1 - bridge < 0:
                dChk = False
                break
            comp = abs(board[row][col] - board[row + 1][col])
            if comp > 1:
                dChk = False
                break
            if comp == 1:
                bChk = True
                if board[row][col] > board[row + 1][col]:
                    nRow = row + 1
                    while nRow < row + bridge:
                        if board[nRow][col] != board[nRow + 1][col] or bridgeCheck[nRow][col] == 2 or bridgeCheck[nRow + 1][col] == 2:
                            bChk = False
                            break
                        nRow += 1
                    if bChk:
                        for r in range(row + 1, row + bridge + 1):
                            bridgeCheck[r][col] = 2
                        row = nRow
                    else:
                        dChk = False
                        break
                elif board[row][col] < board[row + 1][col]:
                    if bridge == 1:
                        if bridgeCheck[row][col] == 2:
                            dChk = False
                            break
                    nRow = row
                    while nRow > row + 1 - bridge:
                        if board[nRow][col] != board[nRow - 1][col] or bridgeCheck[nRow][col] == 2 or bridgeCheck[nRow - 1][col] == 2:
                            bChk = False
                            break
                        nRow -= 1
                    if bChk:
                        for r in range(row + 1 - bridge, row + 1):
                            bridgeCheck[r][col] = 2
                        row += 1
                    else:
                        dChk = False
                        break
            if comp == 0:
                row += 1
        if dChk:
            answer += 1


    print(answer)