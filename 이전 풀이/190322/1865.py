import sys
sys.stdin = open("1865.txt")

for t in range(int(input())):
    N = int(input())

    work = []
    for _ in range(N):
        work.append(list(map(int, input().split())))

    chk = [[0] * N for _ in range(N)]
    multi = 0

    w = 0
    while w < N:
        new = 1
        chkl = [0] * N
        i = 0
        while i < N:
            if chk[w][i] <= N and chkl[i]:
                new *= work[w][i]
                chk[w][i] += 1
                chkl[i] = i
                w += 1
            else:
                i += 1

            if w == N and new > multi:
                multi = new
                w = 0
                break




    print(work)
    print(chk)