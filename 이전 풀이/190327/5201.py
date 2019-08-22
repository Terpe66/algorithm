import sys
sys.stdin = open("5201.txt")

for test in range(int(input())):
    C, T = map(int, input().split())
    c = list(map(int, input().split()))
    t = list(map(int, input().split()))
    c.sort()
    t.sort()

    i = C - 1
    ans = 0
    while i >= 0 and T - 1 >= 0:
        if c[i] <= t[T - 1]:
            ans += c[i]
            T -= 1
        i -= 1

    print(f"#{test + 1} {ans}")