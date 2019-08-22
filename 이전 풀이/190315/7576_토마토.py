import sys
from collections import deque
sys.stdin = open("7576.txt")

for t in range(int(input())):
    width, height = map(int, input().split())
    tomato = [input().split() for _ in range(height)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    Q = deque()
    for row in range(height):
        for col in range(width):
            if tomato[row][col] == "1":
                Q.append((row, col, 0))

    while Q:
        row, col, cnt = Q.popleft()
        for i in range(4):
            x, y = col + dx[i], row + dy[i]
            if 0 <= x < width and 0 <= y < height and tomato[y][x] == "0":
                tomato[y][x] = "1"
                Q.append((y, x, cnt + 1))

    for row in tomato:
        if cnt == -1:
            break
        for col in row:
            if col == "0":
                cnt = -1
                break

    print(cnt)