import sys
sys.stdin = open("17143.txt")

height, width, shark = map(int, input().split())
aquarium = [[0] * width for _ in range(height)]
sharks = [() for _ in range(shark)]

for i in range(shark):
    r, c, s, d, z = map(int, input().split())
    aquarium[r - 1][c - 1] = (s, d, z)
    sharks[i] = (r - 1, c - 1)

answer = 0
for w in range(width):
    g_shark = (100, 0, 0)
    for idx in range(shark):
        r, c = sharks[idx]
        if w == c:
            if r < g_shark[0]:
                g_shark = (r, c, idx)
    r, c, idx = g_shark
    if r < 100:
        answer += aquarium[r][c][2]
        aquarium[r][c] = 0
        sharks[idx] = (-1, -1)

    for idx2 in range(shark):
        r, c = sharks[idx2]
        if r >= 0:
            s, d, z = aquarium[r][c]
            nr, nc, nd = r, c, d
            cnt = s
            while cnt > 0:
                if d == 1:
                    cnt -= 1
                    r -= 1
                    if r == -1:
                        r = 1
                        d = 2
                    continue

                if d == 2:
                    cnt -= 1
                    r += 1
                    if r == height:
                        r = height - 2
                        d = 1
                    continue

                if d == 3:
                    cnt -= 1
                    c += 1
                    if c == width:
                        c = width - 2
                        d = 4
                    continue

                if d == 4:
                    cnt -= 1
                    c -= 1
                    if c == -1:
                        c = 1
                        d = 3
                    continue

            if aquarium[r][c] != 0:
                os, od, oz = aquarium[r][c]
                if oz < z:
                    for idx3 in range(shark):
                        if sharks[idx3] == (r, c):
                            sharks[idx3] = (-1, -1)
                            break
                    aquarium[r][c] = (s, d, z)
                    sharks[idx2] = (r, c)
            else:
                aquarium[r][c] = (s, d, z)
                sharks[idx2] = (r, c)
            if nr != r or nc != c:
                aquarium[nr][nc] = 0
            elif nd != d:
                aquarium[r][c] = (s, d, z)

print(answer)