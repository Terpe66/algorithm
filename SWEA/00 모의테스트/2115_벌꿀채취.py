import sys
sys.stdin = open("2115.txt")


def select(row, col, idx, now):
    global answer

    if idx == 1:
        answer = max(answer, now)
        return

    c = col + M
    for r in range(row, N):
        while c < N - 1:
            select(row, c, 1, now + bee[r][c])
            c += 1
        c = 0


def detail(row, col, idx, now):

    if idx == M:
        calc(row, col)
        return

    for i in range(idx, M):
        if now + select_calc[0][i] <= C:
            select_calc[1][i] = 1
            detail(row, col, i + 1, now + select_calc[0][i])
            select_calc[1][i] = 0
        else:
            calc(row, col)


def calc(row, col):
    point = 0
    for i in range(M):
        if select_calc[1][i] == 1:
            point += select_calc[0][i] ** 2

    bee[row][col] = max(bee[row][col], point)


def go(row, col):

    i = 0
    for c in range(col, col + M):
        select_calc[0][i] = bee[row][c]
        i += 1

    if sum(select_calc[0]) <= C:
        select_calc[1] = [1] * M
        calc(row, col)
        select_calc[1] = [0] * M
    else:
        detail(row, col, 0, 0)


for T in range(int(input())):
    answer = 0
    N, M, C = map(int, input().split())
    bee = [list(map(int, input().split())) for _ in range(N)]
    select_calc = [[0] * M, [0] * M]

    for row in range(N):
        for col in range(N):
            if col + M - 1 < N:
                go(row, col)

    for row in range(N - 1):
        for col in range(N - 1):
            select(row, col, 0, bee[row][col])

    print("#{} {}".format(T + 1, answer))
