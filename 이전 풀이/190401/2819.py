import sys
sys.stdin = open("2819.txt")

def find(row, col, string = ""):
    if len(string) == 7:
        ans.add(string)
        return

    for i in range(4):
        n_row, n_col = row + dir[i], col + dir[3 - i]
        if 0 <= n_row < 4 and 0 <= n_col < 4:
            find(n_row, n_col, string + board[n_row][n_col])

for t in range(int(input())):
    board = [ input().split() for _ in range(4) ]
    dir = (1, -1, 0, 0)
    ans = set()
    for i in range(4):
        for j in range(4):
            find(i, j, board[i][j])

    print(f"#{t + 1} {len(ans)}")