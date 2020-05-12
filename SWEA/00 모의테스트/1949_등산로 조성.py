import sys
sys.stdin = open("1949.txt")

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

for T in range(int(input())):
    answer = 0
    length, deep = map(int, input().split())
    MAP = []
    highest = []
    maxNum = 0
    for i in range(length):
        inputs = list(map(int, input().split()))
        for j in range(length):
            if inputs[j] > maxNum:
                maxNum = inputs[j]
        MAP.append(inputs)

    for i in range(length):
        for j in range(length):
            if MAP[i][j] == maxNum:
                highest.append((i, j, 1, maxNum, deep, [(i, j)]))

    while highest:
        row, col, cnt, num, d, pasts = highest.pop()

        if answer < cnt:
            answer = cnt

        for i in range(4):
            nrow, ncol = row + dr[i], col + dc[i]
            if 0 <= nrow < length and 0 <= ncol < length and (nrow, ncol) not in pasts:
                new = MAP[nrow][ncol]
                if num > new:
                    highest.append((nrow, ncol, cnt + 1, new, d, pasts + [(nrow, ncol)]))
                    continue
                if d != deep:
                    continue
                if num == new:
                    highest.append((nrow, ncol, cnt + 1, new - 1, d - 1, pasts + [(nrow, ncol)]))
                    continue
                if num > new - d:
                    nd = 1
                    while nd <= d:
                        if num > new - nd:
                            break
                        nd += 1
                    if num > new - nd:
                        highest.append((nrow, ncol, cnt + 1, new - nd, d - nd, pasts + [(nrow, ncol)]))

    print("#{} {}".format(T+1, answer))