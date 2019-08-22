import sys
sys.stdin = open("5202.txt")

def find(i, l, cnt):
    global ans

    while i < N:
        if l[line[i][0]] == 0:
            for idx in range(line[i][0], line[i][1]):
                l[idx] = True
            find(i + 1, l, cnt + 1)
            for idx in range(line[i][0], line[i][1]):
                l[idx] = False
        i += 1

    if i == N:
        if ans < cnt:
            ans = cnt
        return


for t in range(int(input())):
    N = int(input())
    line = []
    for _ in range(N):
        i = tuple(map(int, input().split()))
        if i in line:
            N -= 1
            continue
        line.append(i)

    line.sort()
    i = 0
    ans = 0
    while i < N:
        new = [False] * 24
        j = i + 1
        cnt = 1
        for idx in range(line[i][0], line[i][1]):
            new[idx] = True
        find(i + 1, new, cnt)
        i += 1

    print(f"#{t + 1} {ans}")