from collections import deque
import sys
sys.stdin = open("5427.txt")

for t in range(int(input())):
    width, height = map(int, input().split())
    MAP = [" ".join(input()).split() for _ in range(height)]
    human = deque()
    fire = deque()
    for i in range(height):
        for j in range(width):
            if MAP[i][j] == "*":
                fire.append((i, j))
            elif MAP[i][j] == "@":
                human.append((i, j, 0))
    visited = [[False] * width for _ in range(height)]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    chk = False
    while fire or human:
        if fire:
            length = len(fire)
            for _ in range(length):
                fx, fy = fire.popleft()
                for i in range(4):
                    x, y = fx + dx[i], fy + dy[i]
                    if 0 <= x < height and 0 <= y < width and MAP[x][y] == ".":
                        MAP[x][y] = "*"
                        fire.append((x, y))

        if human:
            length = len(human)
            for _ in range(length):
                hx, hy, cnt = human.popleft()
                for i in range(4):
                    x, y = hx + dx[i], hy + dy[i]
                    if 0 <= x < height and 0 <= y < width and MAP[x][y] == "." and visited[x][y] == False:
                        MAP[x][y] = "@"
                        MAP[hx][hy] = "."
                        visited[hx][hy] = True
                        cnt += 1
                        human.append((x, y, cnt))
                        if x in (0, height - 1) or y in (0, width - 1):
                            print(cnt + 1)
                            chk = True
                            break

    if not chk:
        print("IMPOSSIBLE")