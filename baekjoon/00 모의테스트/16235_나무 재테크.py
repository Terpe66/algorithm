from collections import deque

import sys
sys.stdin = open("16235.txt")

dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

for T in range(int(input())):
    length, trees, years = map(int, input().split())
    ground = [[5] * length for _ in range(length)]
    S2D2 = [list(map(int, input().split())) for _ in range(length)]
    treeDict = {}

    for _ in range(trees):
        r, c, y = map(int, input().split())
        treeDict[(r - 1, c - 1)] = deque()
        treeDict[(r - 1, c - 1)].append(y)

    for _ in range(years):
        tempDict = {}
        for key, val in treeDict.items():
            p = 0
            tempDict[key] = deque()
            for i in range(len(val)):
                if ground[key[0]][key[1]] >= val[i]:
                    ground[key[0]][key[1]] -= val[i]
                    val[i] += 1
                    tempDict[key].append(val[i])
                else:
                    p += val[i] // 2
                    val[i] = -1
            ground[key[0]][key[1]] += p

        for key, val in treeDict.items():
            for v in range(len(val)):
                if val[v] % 5 == 0:
                    for j in range(8):
                        r, c = key[0] + dr[j], key[1] + dc[j]
                        if 0 <= r < length and 0 <= c < length:
                            if not tempDict.get((r, c), False):
                                tempDict[(r, c)] = deque()
                            tempDict[(r, c)].appendleft(1)

        for r in range(length):
            for c in range(length):
                ground[r][c] += S2D2[r][c]

        treeDict, tempDict = tempDict, treeDict

    answer = 0
    for val in treeDict.values():
        answer += len(val)

    print(answer)

