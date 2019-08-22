import sys
sys.stdin = open("1491.txt")

for t in range(int(input())):
    N, A, B = map(int, input().split())
    ans = 9999900000
    R = int(N ** 0.5)
    while 1 < R:
        C = N // R
        while R <= C:
            new = A * abs(R - C) + B * (N - R * C)
            ans = min(ans, new)
            C -= 1
        R -= 1
    print(f"#{t + 1} {ans}")
