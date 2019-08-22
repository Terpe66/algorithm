import sys
sys.stdin = open("1974.txt")

for t in range(int(input())):
    sudoku = []

    for _ in range(9):
        sudoku.append(input().split())

    row, col, ans = 0, 0, 1
    while row < 9 and ans:
        while col < 9 and ans:
            S = ""
            cidx, S = col, ""
            if col == 0:
                while cidx < 9:
                    new = sudoku[row][cidx]
                    if new in S:
                        ans = 0
                        break
                    S += new
                    cidx += 1

            ridx, S = row, ""
            if row == 0:
                while ridx < 9:
                    new = sudoku[ridx][col]
                    if new in S:
                        ans = 0
                        break
                    S += new
                    ridx += 1

            ridx, cidx, S = row, col, ""
            if row in (0, 3, 6) and col in (0, 3, 6):
                while ridx < row + 3:
                    new = sudoku[ridx][cidx]
                    if new in S:
                        ans = 0
                        break
                    S += new
                    cidx += 1
                    if cidx >= col + 3:
                        ridx += 1
                        cidx = col
            col += 1
        row += 1
        col = 0

    print(f"#{t+1} {ans}")