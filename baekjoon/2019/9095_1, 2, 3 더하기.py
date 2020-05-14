import sys
sys.stdin = open("9095.txt")

for _ in range(int(input())):
    n = int(input())
    plus = [1, 2, 3]
    c = [0] + [1000000] * n
    for p in plus:
        for j in range(p, n + 1):
            c[j] = min(c[j], c[j - p] + 1)

    if c[n]:
        print(c[n])
    else:
        print(-1)