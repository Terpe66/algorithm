import sys
sys.stdin = open("3752.txt")

for t in range(int(input())):
    N = int(input())
    points = list(map(int, input().split()))
    L = sum(points) + 1
    chk = [100000] * L
    chk[0] = -1

    for i in range(N):
        for j in range(L):
            if chk[j] < i:
                idx = j + points[i]
                if chk[idx] == 100000:
                    chk[idx] = i

    ans = 0
    for i in range(L):
        if chk[i] != 100000:
            ans += 1

    print(f"#{t + 1} {ans}")