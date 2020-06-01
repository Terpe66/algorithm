import sys
sys.stdin = open("4014.txt")

for T in range(int(input())):
    answer = 0
    length, X = map(int, input().split())
    airport = [list(map(int, input().split())) for _ in range(length)]
    check = [[False] * length for _ in range(length)]

    for row in range(length):
        before = airport[row][0]
        col = 1
        break_chk = True
        while col < length:
            if abs(before - airport[row][col]) > 1:
                break_chk = False
                break
            if before < airport[row][col]:
                if col - X < 0:
                    break_chk = False
                    break
                chk = True
                for c in range(col - X, col):
                    if check[row][c] or airport[row][c] != before:
                        chk = False
                        break
                    check[row][c] = True
                if not chk:
                    break_chk = False
                    break
            elif before > airport[row][col]:
                if col + X - 1 >= length:
                    break_chk = False
                    break
                chk = True
                for c in range(col, col + X):
                    if check[row][c] or airport[row][c] != airport[row][col]:
                        chk = False
                        break
                    check[row][c] = True
                if not chk:
                    break_chk = False
                    break
                col = c
            before = airport[row][col]
            col += 1

        if break_chk:
            answer += 1

    check = [[False] * length for _ in range(length)]
    for col in range(length):
        before = airport[0][col]
        row = 1
        break_chk = True
        while row < length:
            if abs(before - airport[row][col]) > 1:
                break_chk = False
                break
            if before < airport[row][col]:
                if row - X < 0:
                    break_chk = False
                    break
                chk = True
                for r in range(row - X, row):
                    if check[r][col] or airport[r][col] != before:
                        chk = False
                        break
                    check[r][col] = True
                if not chk:
                    break_chk = False
                    break
            elif before > airport[row][col]:
                if row + X - 1 >= length:
                    break_chk = False
                    break
                chk = True
                for r in range(row, row + X):
                    if check[r][col] or airport[r][col] != airport[row][col]:
                        chk = False
                        break
                    check[r][col] = True
                if not chk:
                    break_chk = False
                    break
                row = r
            before = airport[row][col]
            row += 1

        if break_chk:
            answer += 1

    print("#{} {}".format(T + 1, answer))
