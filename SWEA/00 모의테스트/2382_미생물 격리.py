import sys
sys.stdin = open("2382.txt")

drc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for T in range(int(input())):
    answer = 0
    length, time, K = map(int, input().split())
    virus = []
    for i in range(K):
        r, c, n, d = map(int, input().split())
        virus.append([r, c, n, d - 1])

    t = 0
    while t < time:
        for i in range(len(virus)):
            r, c, n, d = virus[i]
            y, x = drc[d]
            nr, nc = r + y, c + x
            if nc == 0:
                virus[i][2] //= 2
                virus[i][3] = 3
            elif nc == length - 1:
                virus[i][2] //= 2
                virus[i][3] = 2
            elif nr == 0:
                virus[i][2] //= 2
                virus[i][3] = 1
            elif nr == length - 1:
                virus[i][2] //= 2
                virus[i][3] = 0
            virus[i][0], virus[i][1] = nr, nc

        temp = {}
        for i in range(len(virus)):
            temp.setdefault((virus[i][0], virus[i][1]), []).append((virus[i][2], i))

        check = False
        for key, val in temp.items():
            if len(val) > 1:
                check = True
                val.sort()
                main = val[-1]
                point = 0
                for s in val:
                    if s != main:
                        r, c, n, d = virus[s[1]]
                        point += n
                        virus[s[1]] = [0, 0, 0, 0]
                virus[main[1]][2] += point

        if check:
            for i in range(len(virus) - 1, -1, -1):
                r, c, n, d = virus[i]
                if r == 0 and c == 0:
                    virus.pop(i)
        t += 1

    for i in range(len(virus)):
        answer += virus[i][2]

    print("#{} {}".format(T + 1, answer))
