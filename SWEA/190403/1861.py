import sys
sys.stdin = open("1861.txt")

for t in range(int(input())):
    size = int(input())
    board = [list(map(int, input().split())) for _ in range(size)]
    ans = cnt = 0

    dir = [-1, 1, 0, 0]
    Q = []
    visited = [[True] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if visited[i][j]:
                Q.append((i, j))
                visited[i][j] = False
                new = 1
                while Q:
                    row, col = Q.pop()
                    if new > cnt:
                        cnt = new
                        ans = min(board[i][j], board[row][col])
                    elif new == cnt:
                        if ans > min(board[i][j], board[row][col]):
                            ans = min(board[i][j], board[row][col])

                    for idx in range(4):
                        nrow, ncol = row + dir[idx], col + dir[3 - idx]
                        if 0 <= nrow < size and 0 <= ncol < size and abs(board[nrow][ncol] - board[row][col]) == 1 and visited[nrow][ncol]:
                            Q.append((nrow, ncol))
                            visited[nrow][ncol] = False
                            new += 1

    print(f"#{t + 1} {ans} {cnt}")