import sys
sys.stdin = open("workshop.txt")

for t in range(10):
    people, start = map(int, input().split())
    _ = list(map(int, input().split()))
    line = [[] for x in range(people+1)]
    count = [-1] * (people+1)
    for i in range(0, people, 2):
        if _[i+1] not in line[i]:
            line[_[i]].append(_[i+1])
    for l in line:
        l.sort()

    Q = [[start]]
    sub = []
    cnt = 0
    while Q:
        idx = Q.pop(0)
        for i in idx:
            if count[i] == -1:
                count[i] = cnt
            if line[i]:
                for j in line[i]:
                    sub.append(j)
                line[i] = []
        if sub:
            Q.append(sub)
            sub = []
        cnt += 1
    ans = [0, 0]
    for i in range(people+1):
        if ans[1] <= count[i]:
            ans = [i, count[i]]

    print(f"#{t+1} {ans[0]}")


