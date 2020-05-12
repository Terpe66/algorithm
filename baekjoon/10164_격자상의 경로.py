import sys
sys.stdin = open("10164.txt")

N, M, K = map(int, input().split())
if K:
    mid_row = (K - 1) // M
    mid_col = (K - 1) - M * mid_row
else:
    mid_row = mid_col = 0
ans1 = ans2 = 1

LIST1 = [[1] * M for _ in range(mid_row + 1)]
j = 1
for i in range(1, mid_row + 1):
    for j in range(1, mid_col + 1):
        LIST1[i][j] = LIST1[i][j - 1] + LIST1[i - 1][j]
    ans1 = LIST1[i][j]

LIST2 = [[1] * (M + 1) for _ in range(N + 1)]
for i in range(mid_row + 1, N):
    for j in range(mid_col + 1, M):
        LIST2[i][j] = LIST2[i][j - 1] + LIST2[i - 1][j]
    ans2 = LIST2[i][j]
print(ans1 * ans2)