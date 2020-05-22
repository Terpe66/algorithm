import sys
sys.stdin = open("17144.txt")


def dust(row, col, cur, next):

    cnt = 0
    for y, x in drc:
        nr, nc = row + y, col + x
        if 0 <= nr < height and 0 <= nc < width and room[cur][nr][nc] != -1:
            room[next][nr][nc] += room[cur][row][col] // 5
            cnt += 1

    room[next][row][col] += room[cur][row][col] - (room[cur][row][col] // 5 * cnt)
    room[cur][row][col] = 0


def wind_on(mc, idx):

    uRow, uCol = mc[0]
    dRow, dCol = mc[1]

    temp = room[idx][uRow][0]
    if temp == -1:
        temp = 0
    for r in range(uRow, 0, -1):
        room[idx][r][0] = room[idx][r - 1][0]

    for c in range(width - 1):
        room[idx][0][c] = room[idx][0][c + 1]

    for r in range(uRow):
        room[idx][r][-1] = room[idx][r + 1][-1]

    for c in range(width - 1, 1, -1):
        room[idx][uRow][c] = room[idx][uRow][c - 1]

    room[idx][uRow][1] = temp

    temp = room[idx][dRow][0]
    if temp == -1:
        temp = 0
    for r in range(dRow, height - 1):
        room[idx][r][0] = room[idx][r + 1][0]

    for c in range(width - 1):
        room[idx][-1][c] = room[idx][-1][c + 1]

    for r in range(height - 1, dRow, -1):
        room[idx][r][-1] = room[idx][r - 1][-1]

    for c in range(width - 1, 1, -1):
        room[idx][dRow][c] = room[idx][dRow][c - 1]

    room[idx][dRow][1] = temp
    room[idx][uRow][uCol] = -1
    room[idx][dRow][dCol] = -1


drc = [(-1, 0), (0, -1), (1, 0), (0, 1)]

for T in range(int(input())):
    height, width, time = map(int, input().split())
    room = [[], [[0] * width for _ in range(height)]]
    wind = []
    for i in range(height):
        inputs = list(map(int, input().split()))
        for j in range(width):
            if inputs[j] == -1:
                wind.append((i, j))
                room[1][i][j] = -1
        room[0].append(inputs)

    cur = t = 0
    while t < time:
        next = (cur + 1) % 2

        for row in range(height):
            for col in range(width):
                if room[cur][row][col] > 0:
                    dust(row, col, cur, next)

        wind_on(wind, next)

        t += 1
        cur = next

    answer = 0
    for row in range(height):
        for col in range(width):
            answer += room[next][row][col]
    answer += 2

    print(answer)