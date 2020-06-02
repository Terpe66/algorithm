from collections import deque
import sys
sys.stdin = open("5653.txt")


def kill_virus(rs, re, cs, ce):
    for r in range(rs - 2, re + 3):
        for c in range(cs - 2, ce + 3):
            if bowl[r][c] < -1:
                bowl[r][c] += 1


def reset_bowl(rs, re, cs, ce):
    point = 0
    for r in range(rs - 2, re + 3):
        for c in range(cs - 2, ce + 3):
            if bowl[r][c] > 0 or bowl[r][c] < -1:
                point += 1
            bowl[r][c] = 0

    return point


bowl = [[0] * 650 for _ in range(650)]
drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for T in range(int(input())):
    answer = 0
    height, width, K = map(int, input().split())

    virus = {}
    for i in range(1, 11):
        virus[i] = deque()

    status = [i for i in range(11)]
    temp = [list(map(int, input().split())) for _ in range(height)]
    for r in range(height):
        for c in range(width):
            bowl[300 + r][300 + c] = temp[r][c]
            if temp[r][c] > 0:
                virus[temp[r][c]].append((300 + r, 300 + c))

    rs, re, cs, ce = 300, 300 + height, 300, 300 + width

    time = 1
    while time <= K:
        for i in range(10, 0, -1):
            if status[i] == 0:
                temp = deque()
                while virus[i]:
                    row, col = virus[i].popleft()
                    if rs > row:
                        rs = row
                    if re < row:
                        re = row
                    if cs > col:
                        cs = col
                    if ce < col:
                        ce = col

                    for y, x in drc:
                        nrow, ncol = row + y, col + x
                        if 0 == bowl[nrow][ncol]:
                            bowl[nrow][ncol] = bowl[row][col]
                            temp.append((nrow, ncol))
                    bowl[row][col] = bowl[row][col] * -1 - 1

                virus[i] = temp
                status[i] = i
            else:
                status[i] -= 1
        time += 1
        kill_virus(rs, re, cs, ce)

    answer = reset_bowl(rs, re, cs, ce)
    print("#{} {}".format(T + 1, answer))
