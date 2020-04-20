import sys
sys.stdin = open("2667.txt")

def find(row, col):
    global ans, size, cnt

    visited[row][col] = True
    cnt += 1
    if col + 1 < size and apart[row][col + 1] == "1" and not visited[row][col + 1]:
        find(row, col + 1)
    if row + 1 < size and apart[row + 1][col] == "1" and not visited[row + 1][col]:
        find(row + 1, col)
    if col - 1 >= 0 and apart[row][col - 1] == "1" and not visited[row][col - 1]:
        find(row, col - 1)
    if row - 1 >= 0 and apart[row - 1][col] == "1" and not visited[row - 1][col]:
        find(row - 1, col)

size = int(input())
apart = []
ans = 0
for _ in range(size):
    apart.append(" ".join(input()).split())
visited = [[False] * size for _ in range(size)]
C = []
for row in range(size):
    for col in range(size):
        if apart[row][col] != "0" and visited[row][col] == False:
            cnt = 0
            find(row, col)
            ans += 1
            C.append(cnt)
C.sort()
print(ans)
for c in C:
    print(c)