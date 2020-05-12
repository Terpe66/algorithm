import sys
sys.stdin = open("3074.txt")

for t in range(int(input())):
    judge, guest = map(int, input().split())
    time = [int(input()) for _ in range(judge)]
    l, r = 0, max(time) * guest
    mid = (l + r) // 2
    while l != r:
        i = new = 0
        while i < judge:
            new += mid // time[i]
            i += 1
        if new >= guest:
            r = mid
        else:
            l = mid + 1
        mid = (l + r) // 2

    print(f"#{t + 1} {l}")