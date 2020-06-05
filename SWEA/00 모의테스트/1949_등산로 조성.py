import sys
sys.stdin = open("1949.txt")


drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for T in range(int(input())):
    answer = 0
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    start = []
    m = 0
    for r in range(N):
        for c in range(N):
            if mountain[r][c] > m:
                start = [(r, c)]
                m = mountain[r][c]
            elif mountain[r][c] == m:
                start.append((r, c))

    for row, col in start:
        temp = [(row, col, K, mountain[row][col], [(row, col)])]
        while temp:
            r, c, k, now, past = temp.pop()

            answer = max(answer, len(past))

            for y, x in drc:
                nr, nc = r + y, c + x
                if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in past:
                    new = mountain[nr][nc]
                    if now > new:
                        temp.append((nr, nc, k, new, past + [(nr, nc)]))
                    elif k and new - k < now <= new:
                        temp.append((nr, nc, 0, new - (new - now) - 1, past + [(nr, nc)]))

    print("#{} {}".format(T + 1, answer))
