from collections import deque
import sys
sys.stdin = open("17142.txt")


def reset():
    for r in range(length):
        for c in range(length):
            visit[r][c] = 0xffffffff


def move_virus(selected):
    global answer

    select = deque()
    for j in range(virusNum):
        r, c, cnt = virus[selected[j]]
        select.append((r, c, cnt))
        visit[r][c] = 0

    while select:
        r, c, cnt = select.popleft()

        for y, x in drc:
            nr, nc = r + y, c + x
            if 0 <= nr < length and 0 <= nc < length and lab[nr][nc] != -1 and visit[nr][nc] > cnt + 1:
                visit[nr][nc] = cnt + 1
                select.append((nr, nc, cnt + 1))

    tmp = 0
    for r in range(length):
        if tmp == -1:
            break
        for c in range(length):
            if lab[r][c] == -1 or lab[r][c] == 2:
                continue

            if visit[r][c] == 0xffffffff:
                tmp = -1
                break

            tmp = max(tmp, visit[r][c])

    if tmp >= 0:
        answer = min(answer, tmp)

    reset()


def select_virus(idx, n, selected):
    if n == virusNum:
        move_virus(selected)
        return

    for i in range(idx, len(virus)):
        select_virus(i + 1, n + 1, selected + [i])


drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for T in range(int(input())):
    answer = 0xffffffff
    length, virusNum = map(int, input().split())
    virus = []
    lab = []
    visit = [[0xffffffff] * length for _ in range(length)]
    for i in range(length):
        inputs = list(map(int, input().split()))
        for j in range(length):
            if inputs[j] == 2:
                virus.append((i, j, 0))
            elif inputs[j] == 1:
                inputs[j] = -1
        lab.append(inputs)

    select_virus(0, 0, [])

    if answer == 0xffffffff:
        answer = -1
    print(answer)
