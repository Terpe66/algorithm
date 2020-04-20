import sys
sys.stdin = open("1018.txt")

# for t in range(int(input())):
height, width = map(int, input().split())
board = [list(input()) for _ in range(height)]
row = col = 0
ans = 32
while row + 7 < height:
    sub = 0
    if board[row][col] == "W":
        for r in range(row, row + 8):
            for c in range(col + 1, col + 8):
                board

    if ans > sub:
        ans = sub

    col += 1
    if col + 7 >= width:
        col = 0
        row += 1

print(ans)