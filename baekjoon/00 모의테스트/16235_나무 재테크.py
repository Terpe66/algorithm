import sys
sys.stdin = open("16235.txt")

drc = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

for T in range(int(input())):
    length, trees, years = map(int, input().split())
    ground = [[[5, []] for _ in range(length)] for _ in range(length)]
    S2D2 = [list(map(int, input().split())) for _ in range(length)]

    for _ in range(trees):
        r, c, y = map(int, input().split())
        ground[r - 1][c - 1][1].append(y)

    for _ in range(years):
        for row in range(length):
            for col in range(length):
                p = 0
                idx = 0
                for i in range(len(ground[row][col][1])):
                    if ground[row][col][0] >= ground[row][col][1][i]:
                        ground[row][col][0] -= ground[row][col][1][i]
                        ground[row][col][1][i] += 1
                        idx += 1
                    else:
                        p += ground[row][col][1][i] // 2
                ground[row][col][0] += p
                while idx < len(ground[row][col][1]):
                    ground[row][col][1].pop()

        for row in range(length):
            for col in range(length):
                ground[row][col][0] += S2D2[row][col]
                cnt = 0
                for i in ground[row][col][1]:
                    if i % 5 == 0:
                        cnt += 1
                if cnt:
                    for y, x in drc:
                        r, c = row + y, col + x
                        if 0 <= r < length and 0 <= c < length:
                            ground[r][c][1] = [1] * cnt + ground[r][c][1]

    answer = 0
    for row in range(length):
        for col in range(length):
            answer += len(ground[row][col][1])

    print(answer)