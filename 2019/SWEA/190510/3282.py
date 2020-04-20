import sys
sys.stdin = open("3282.txt")

def pack(i, volume, value):
    global ans

    idx = i
    while idx < N:
        new_volume = volume + volNval[idx][0]
        if new_volume > K:
            return
        if visit[idx] == False:
            visit[idx] = True
            pack(idx + 1, new_volume, value + volNval[idx][1])
            visit[idx] = False
        idx += 1

    if value > ans:
        ans = value
    return


for T in range(int(input())):
    N, K = map(int, input().split())
    volNval = [tuple(map(int, input().split())) for _ in range(N)]
    volNval.sort()
    visit = [False for _ in range(N)]
    ans = 0

    pack(0, 0, 0)

    print(f"#{T + 1} {ans}")