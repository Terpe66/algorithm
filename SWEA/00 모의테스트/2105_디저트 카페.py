import sys
sys.stdin = open("2105.txt")

for T in range(int(input())):
    length = int(input())
    cafe = [list(map(int, input().split())) for _ in range(length)]
    answer = -1
    dr = [1, 1, -1, -1]
    dc = [1, -1, -1, 1]
    dw = [0, 1, 2, 3]

    for row in range(length - 1):
        for col in range(1, length - 1):
            S = [(row, col, 0, [cafe[row][col]])]
            while S:
                r, c, d, dessert = S.pop()

                if r == row and c == col and answer < len(dessert) > 1:
                    answer = len(dessert)
                    continue

                if d == 0:
                    nr, nc = r + dr[0], c + dc[0]
                    if 0 <= nr < length and 0 <= nc < length and cafe[nr][nc] not in dessert:
                        S.append((nr, nc, 0, dessert[:] + [cafe[nr][nc]]))
                    if len(dessert) > 1:
                        nr, nc = r + dr[1], c + dc[1]
                        if 0 <= nr < length and 0 <= nc < length and cafe[nr][nc] not in dessert:
                            S.append((nr, nc, 1, dessert[:] + [cafe[nr][nc]]))
                if d == 1:
                    nr, nc = r + dr[1], c + dc[1]
                    if 0 <= nr < length and 0 <= nc < length and cafe[nr][nc] not in dessert:
                        S.append((nr, nc, 1, dessert[:] + [cafe[nr][nc]]))
                    nr, nc = r + dr[2], c + dc[2]
                    if 0 <= nr < length and 0 <= nc < length and cafe[nr][nc] not in dessert:
                        S.append((nr, nc, 2, dessert[:] + [cafe[nr][nc]]))
                if d == 2:
                    nr, nc = r + dr[2], c + dc[2]
                    if 0 <= nr < length and 0 <= nc < length and cafe[nr][nc] not in dessert:
                        S.append((nr, nc, 2, dessert[:] + [cafe[nr][nc]]))
                    if abs(row - r) == abs(col - c):
                        nr, nc = r + dr[3], c + dc[3]
                        d = 3
                        if 0 <= nr < length and 0 <= nc < length and cafe[nr][nc] not in dessert:
                            S.append((nr, nc, 3, dessert[:] + [cafe[nr][nc]]))
                if d == 3:
                    nr, nc = r + dr[3], c + dc[3]
                    if 0 <= nr < length and 0 <= nc < length and cafe[nr][nc] not in dessert:
                        S.append((nr, nc, 3, dessert[:] + [cafe[nr][nc]]))
                    if nr == row and nc == col:
                        S.append((nr, nc, 3, dessert[:]))



    print("#{} {}".format(T+1, answer))