from collections import deque

import sys
sys.stdin = open("16236.txt")


def check(size):
    chk = False
    for row in range(length):
        for col in range(length):
            if 0 < sea[row][col] < size:
                chk = True
            visit[row][col] = True

    return chk


drc = [(-1, 0), (0, -1), (0, 1), (1, 0)]

for T in range(int(input())):
    answer = 0
    length = int(input())
    sea = []
    visit = [[True] * length for _ in range(length)]

    for i in range(length):
        inputs = list(map(int, input().split()))
        for j in range(length):
            if inputs[j] == 9:
                shark = (i, j)
                inputs[j] = 0
        sea.append(inputs)

    size = 2
    sizeCount = 2
    while check(size):

        temp = deque()
        temp.append((shark[0], shark[1], 0))
        visit[shark[0]][shark[1]] = False
        targetCnt = 0xffffffff
        target = (length, length)
        chk = True
        while temp:
            r, c, cnt = temp.popleft()

            for y, x in drc:
                nr, nc = r + y, c + x
                if 0 <= nr < length and 0 <= nc < length and sea[nr][nc] <= size and visit[nr][nc]:
                    visit[nr][nc] = False
                    if 0 < sea[nr][nc] < size:
                        chk = False
                        if cnt + 1 < targetCnt:
                            target = (nr, nc)
                            targetCnt = cnt + 1
                        elif cnt + 1 == targetCnt:
                            if nr < target[0]:
                                target = (nr, nc)
                            elif nr == target[0] and nc < target[1]:
                                target = (nr, nc)
                    else:
                        temp.append((nr, nc, cnt + 1))

        if chk:
            break

        answer += targetCnt
        sea[target[0]][target[1]] = 0
        shark = target
        sizeCount -= 1

        if sizeCount == 0:
            size += 1
            sizeCount = size

    print(answer)


