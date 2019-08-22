from collections import deque
import sys
sys.stdin = open("1890.txt")

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

board[N-1][N-1] = 1
c =[[0] * N for _ in range(N)]
c[0][0] = 1
for row in range(N):
    for col in range(N):
        if row + board[row][col] < N:
            c[row + board[row][col]][col] += c[row][col]
        if col + board[row][col] < N:
            c[row][col + board[row][col]] += c[row][col]

print(c[N-1][N-1])

# Q = deque()
# Q.append((0, 0))
# ans = 0
# while Q:
#     x, y = Q.popleft()
#     n = int(board[x][y])
#     if y + n < N:
#         if board[x][y + n] != "0":
#             Q.append((x, y + n))
#         else:
#             ans += 1
#             board[x][y] = "0"
#     if x + n < N:
#         if board[x + n][y] != "0":
#             Q.append((x + n, y))
#         else:
#             ans += 1
#             board[x][y] = "0"
# print(ans)