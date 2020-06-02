from collections import deque

import sys
sys.stdin = open("1249.txt")

drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for T in range(int(input())):
    answer = 0
    length = int(input())
    road = [list(map(int, input())) for _ in range(length)]

    check_road = [[0xffffffff] * length for _ in range(length)]
    check_road[0][0] = 0

    Q = deque()
    Q.append((0, 0))
    while Q:
        row, col = Q.popleft()

        for y, x in drc:
            nrow, ncol = row + y, col + x
            if 0 <= nrow < length and 0 <= ncol < length and check_road[nrow][ncol] > check_road[row][col] + road[nrow][ncol]:
                check_road[nrow][ncol] = check_road[row][col] + road[nrow][ncol]
                Q.append((nrow, ncol))

    print("#{} {}".format(T + 1, check_road[length - 1][length - 1]))
