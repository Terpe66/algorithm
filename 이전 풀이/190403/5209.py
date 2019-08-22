import sys
sys.stdin = open("5209.txt")

def find(idx = 0, new = 0):
    global ans

    if idx == N:
        if ans > new:
            ans = new
        return

    for i in range(N):
        if chk[i] == False:
            chk[i] = True
            find(idx + 1, new + LIST[idx][i])
            chk[i] = False

for t in range(int(input())):
    N = int(input())
    LIST = [list(map(int, input().split())) for _ in range(N)]
    ans = 0xffffff
    chk = [False] * N

    find()
    print(f"#{t + 1} {ans}")