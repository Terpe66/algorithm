import sys
import time
sys.stdin = open("17779.txt")


def fill(r, c, value):
    if r < 0 or r >= length or c < 0 or c >= length:
        return
    if copy_city[r][c] != 0:
        return
    copy_city[r][c] = value
    fill(r - 1, c, value)
    fill(r + 1, c, value)
    fill(r, c - 1, value)
    fill(r, c + 1, value)


def reset():
    for i in range(length):
        for j in range(length):
            copy_city[i][j] = 0


def calc_city():
    answer = 0xffffffff

    for x in range(length - 2):
        for y in range(1, length - 1):
            d1 = 1
            while x + d1 <= length - 2 and 0 <= y - d1:
                d2 = 1
                while x + d1 + d2 <= length - 1 and y + d2 <= length - 1:
                    reset()
                    for i in range(d1 + 1):
                        copy_city[x + i][y - i] = 5
                        copy_city[x + d2 + i][y + d2 - i] = 5
                    for i in range(d2 + 1):
                        copy_city[x + i][y + i] = 5
                        copy_city[x + d1 + i][y - d1 + i] = 5
                    for r in range(x - 1, -1, -1):
                        copy_city[r][y] = 1
                    for c in range(y + d2 + 1, length):
                        copy_city[x + d2][c] = 2
                    for c in range(y - d1 - 1, -1, -1):
                        copy_city[x + d1][c] = 3
                    for r in range(x + d1 + d2 + 1, length):
                        copy_city[r][y - d1 + d2] = 4

                    fill(0, 0, 1)
                    fill(0, length - 1, 2)
                    fill(length - 1, 0, 3)
                    fill(length - 1, length - 1, 4)

                    for r in range(length):
                        for c in range(length):
                            cities[copy_city[r][c] - 1] += city[r][c]

                    answer = min(answer, max(cities) - min(cities))

                    for i in range(5):
                        cities[i] = 0

                    d2 += 1
                d1 += 1

    return answer


for T in range(int(input())):
    length = int(input())
    city = [list(map(int, input().split())) for _ in range(length)]
    copy_city = [[0] * length for _ in range(length)]
    cities = [0] * 5

    print(calc_city())
