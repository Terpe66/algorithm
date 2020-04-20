import sys
sys.stdin = open("1953.txt")

from collections import deque

for T in range(int(input())):
    height, width, row, col, time = map(int, input().split())
    Map = []
    chk = []
    for _ in range(height):
        Map.append(input().split())
        chk.append([False] * width)
    chk[row][col] = True
    ans = 1
    time -= 1
    Q = deque()
    Q.append((row, col, time))
    dir = [-1, 1, 0, 0]
    pipe = [("1", "2", "5", "6"), ("1", "2", "4", "7"), ("1", "3", "6", "7"), ("1", "3", "4", "5")]
    while Q:
        r, c, t = Q.popleft()
        spot = Map[r][c]
        if t:
            for i in range(4):
                C = False
                if spot == "1":
                    nrow, ncol = r + dir[i], c + dir[3 - i]
                    if 0 <= nrow < height and 0 <= ncol < width and Map[nrow][ncol] in pipe[i] and chk[nrow][ncol] == False:
                        C = True
                elif spot == "2" and i <= 1:
                    nrow, ncol = r + dir[i], c + dir[3 - i]
                    if 0 <= nrow < height and 0 <= ncol < width and Map[nrow][ncol] in pipe[i] and chk[nrow][ncol] == False:
                        C = True
                elif spot == "3" and i >= 2:
                    nrow, ncol = r + dir[i], c + dir[3 - i]
                    if 0 <= nrow < height and 0 <= ncol < width and Map[nrow][ncol] in pipe[i] and chk[nrow][ncol] == False:
                        C = True
                elif spot == "4" and i % 2 == 0:
                    nrow, ncol = r + dir[i], c + dir[3 - i]
                    if 0 <= nrow < height and 0 <= ncol < width and Map[nrow][ncol] in pipe[i] and chk[nrow][ncol] == False:
                        C = True
                elif spot == "5" and 1 <= i <= 2:
                    nrow, ncol = r + dir[i], c + dir[3 - i]
                    if 0 <= nrow < height and 0 <= ncol < width and Map[nrow][ncol] in pipe[i] and chk[nrow][ncol] == False:
                        C = True
                elif spot == "6" and i % 2:
                    nrow, ncol = r + dir[i], c + dir[3 - i]
                    if 0 <= nrow < height and 0 <= ncol < width and Map[nrow][ncol] in pipe[i] and chk[nrow][ncol] == False:
                        C = True
                elif spot == "7":
                    if i == 0 or i == 3:
                        nrow, ncol = r + dir[i], c + dir[3 - i]
                        if 0 <= nrow < height and 0 <= ncol < width and Map[nrow][ncol] in pipe[i] and chk[nrow][ncol] == False:
                            C = True
                if C:
                    Q.append((nrow, ncol, t - 1))
                    chk[nrow][ncol] = True
                    ans += 1

    print(f"#{T + 1} {ans}")