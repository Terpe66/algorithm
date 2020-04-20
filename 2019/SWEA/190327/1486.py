import sys
sys.stdin = open("1486.txt")

for t in range(int(input())):
    N, B = map(int, input().split())
    key = list(map(int, input().split()))
    ans = 200000
    for i in range(1 << N):
        go = 0
        for j in range(N):
            if i & (1 << j):
                go += key[j]
        if go >= B:
            go = go - B
            ans = min(ans, go)

    print(f"#{t + 1} {ans}")