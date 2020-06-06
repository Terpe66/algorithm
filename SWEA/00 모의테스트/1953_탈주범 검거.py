import sys
sys.stdin = open("1953.txt")

from collections import deque

drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for T in range(int(input())):
    answer = 1
    height, width, hole_row, hole_col, left = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(height)]
    time = [[0xffffffff] * width for _ in range(height)]

    thief = deque()
    thief.append((hole_row, hole_col))
    time[hole_row][hole_col] = 1
    while thief:
        row, col = thief.popleft()

        if time[row][col] == left:
            continue

        for i in range(4):
            y, x = drc[i]
            nrow, ncol = row + y, col + x
            if 0 <= nrow < height and 0 <= ncol < width and time[nrow][ncol] == 0xffffffff and tunnel[nrow][ncol] > 0:
                check = False
                if i == 0 and tunnel[row][col] in (1, 2, 4, 7) and tunnel[nrow][ncol] in (1, 2, 5, 6):
                    check = True
                elif i == 1 and tunnel[row][col] in (1, 3, 4, 5) and tunnel[nrow][ncol] in (1, 3, 6, 7):
                    check = True
                elif i == 2 and tunnel[row][col] in (1, 2, 5, 6) and tunnel[nrow][ncol] in (1, 2, 4, 7):
                    check = True
                elif i == 3 and tunnel[row][col] in (1, 3, 6, 7) and tunnel[nrow][ncol] in (1, 3, 4, 5):
                    check = True
                if check:
                    thief.append((nrow, ncol))
                    time[nrow][ncol] = time[row][col] + 1
                    answer += 1

    print("#{} {}".format(T + 1, answer))
