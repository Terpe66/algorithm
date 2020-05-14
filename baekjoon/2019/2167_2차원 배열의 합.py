import sys
sys.stdin = open("2167.txt")

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

K = int(input())
for _ in range(K):
    inputs = tuple(map(int, input().split()))
    i, j = inputs[0]-1, inputs[1]-1
    ans = 0
    while i < inputs[2]:
        while j < inputs[3]:
            ans += board[i][j]
            j += 1
        i += 1
        j = inputs[1]-1
    print(ans)