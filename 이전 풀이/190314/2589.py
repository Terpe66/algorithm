import sys
sys.stdin = open("2589.txt")

from collections import deque

height, width = map(int, sys.stdin.readline().rstrip().split())
MAP = []
MAP.append(["W"] * (width + 2))
for _ in range(height):
    MAP.append(["W"] + list(sys.stdin.readline().rstrip()) + ["W"])
MAP.append(["W"] * (width + 2))
visited = [[True] * (width + 1) for _ in range(height + 1)]
dst = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
max_cnt = 0

queue = [0] * 2500
iEnq = 0
iDeq = 0
for row in range(1, height + 1):
    for col in range(1, width + 1):
        if MAP[row][col] == "L":
            cnt = 0
            #dst.append((row, col, 0))
            iEnq = 0
            iDeq = 0
            queue[iEnq] = (row, col, 0)
            iEnq += 1
            if visited[row][col]:
                chk = False
            else:
                chk = True
            visited[row][col] = chk
            while iDeq != iEnq:
            #while dst:
                # r, c, cnt = dst.popleft()
                r, c, cnt = queue[iDeq]
                iDeq += 1
                for i in range(4):
                    nrow, ncol = r + dy[i], c + dx[i]
                    if MAP[nrow][ncol] == "L":
                        if visited[nrow][ncol] != chk:
                            # dst.append((nrow, ncol, cnt + 1))
                            queue[iEnq] = (nrow, ncol, cnt + 1)
                            iEnq += 1
                            visited[nrow][ncol] = chk
            if max_cnt < cnt:
                max_cnt = cnt

print(max_cnt)