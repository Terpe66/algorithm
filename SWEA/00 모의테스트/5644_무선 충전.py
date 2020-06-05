import sys
sys.stdin = open("5644.txt")


drc = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]
for T in range(int(input())):
    answer = 0
    time, bc = map(int, input().split())
    board = [[[0] * bc for _ in range(19)] for _ in range(19)]
    person = [list(map(int, input().split())), list(map(int, input().split()))]
    for i in range(bc):
        c, r, rg, power = map(int, input().split())
        r, c = r + 3, c + 3
        crg = rg
        for row in range(r - rg, r + 1):
            for col in range(c - rg + crg, c + rg + 1 - crg):
                board[row][col][i] = power
            crg -= 1
        crg = 1
        for row in range(r + 1, r + rg + 1):
            for col in range(c - rg + crg, c + rg + 1 - crg):
                board[row][col][i] = power
            crg += 1

    frow = fcol = 4
    srow = scol = 13
    first = second = 0
    for t in range(time + 1):
        fmax = 0
        fidx = 0
        for i in range(bc):
            if fmax < board[frow][fcol][i]:
                fmax = board[frow][fcol][i]
                fidx = i

        smax = 0
        sidx = 0
        for i in range(bc):
            if smax < board[srow][scol][i]:
                smax = board[srow][scol][i]
                sidx = i

        point = fmax + smax
        if fmax == smax and fidx == sidx:
            fcomp = scomp = 0
            for i in range(bc):
                if fcomp < board[frow][fcol][i] and i != fidx:
                    fcomp = board[frow][fcol][i]

            for i in range(bc):
                if scomp < board[srow][scol][i] and i != sidx:
                    scomp = board[srow][scol][i]

            comp = fmax // 2
            point = max(comp * 2, fmax + scomp, smax + fcomp)

        answer += point

        if t < time:
            fidx, sidx = person[0][t], person[1][t]
            frow, fcol = frow + drc[fidx][0], fcol + drc[fidx][1]
            srow, scol = srow + drc[sidx][0], scol + drc[sidx][1]

    print("#{} {}".format(T + 1, answer))
