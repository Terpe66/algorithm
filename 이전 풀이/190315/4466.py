import sys
sys.stdin = open("4466.txt")

for t in range(int(input())):
    P, select = map(int, input().split())
    points = list(map(int, input().split()))
    point = 0
    idx = cnt = 0
    while idx < P:
        p = points[idx]
        i, s = cnt + 1, select - 1
        while i < P and s:
            p += points[i]
            s -= 1
        if P - cnt - 1 <= 0:
            idx += 1
            cnt = idx
        else:
            cnt += 1
        if point < p:
            point = p

    print(f"#{t + 1} {point}")