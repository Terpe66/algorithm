import sys
import time
sys.stdin = open("17779.txt")


def calc_city(row, col, right_row, right_col, bottom_row, bottom_col, left_row, left_col):
    global answer

    r, c = row, col
    while r <= left_row and c >= left_col:
        copy_city[r][c] = 4
        c -= 1
        r += 1
    r, c = row + 1, col + 1
    while r <= right_row and c <= right_col:
        copy_city[r][c] = 4
        c += 1
        r += 1
    r, c = left_row + 1, left_col + 1
    while r <= bottom_row and c <= bottom_col:
        copy_city[r][c] = 4
        c += 1
        r += 1
    r, c = right_row + 1, right_col - 1
    while r <= bottom_row and c >= bottom_col:
        copy_city[r][c] = 4
        c -= 1
        r += 1

    for r in range(row + 1, bottom_row):
        before = 0
        for c in range(left_col, right_col + 1):
            if before == 4 and copy_city[r][c] == 4:
                break

            if before == 4:
                copy_city[r][c] = 4

            if copy_city[r][c] == 4:
                before = 4

    for r in range(row):
        for c in range(col + 1, length):
            copy_city[r][c] = 1

    tmp = 0
    for r in range(row, right_row + 1):
        for c in range(col + 1 + tmp, length):
            copy_city[r][c] = 1
        tmp += 1

    tmp = bottom_col - left_col
    for r in range(left_row, bottom_row + 1):
        for c in range(bottom_col - tmp):
            copy_city[r][c] = 2
        tmp -= 1

    for r in range(bottom_row + 1, length):
        for c in range(bottom_col):
            copy_city[r][c] = 2

    tmp = right_col - bottom_col
    for r in range(right_row + 1, bottom_row + 1):
        for c in range(bottom_col + tmp, length):
            copy_city[r][c] = 3
        tmp -= 1

    for r in range(bottom_row + 1, length):
        for c in range(bottom_col, length):
            copy_city[r][c] = 3

    for r in range(length):
        for c in range(length):
            cities[copy_city[r][c]] += city[r][c]
            copy_city[r][c] = 0

    answer = min(answer, max(cities) - min(cities))

    for i in range(5):
        cities[i] = 0


def make_line(row, col, left_deep, right_deep):

    left_row, left_col = row + left_deep, col - left_deep
    right_row, right_col = row + right_deep, col + right_deep
    bottom_row, bottom_col = right_row + left_deep, right_col - left_deep

    if left_row >= length or left_col < 0 or right_row >= length or right_col >= length or bottom_row >= length or bottom_col >= length:
        return

    calc_city(row, col, right_row, right_col, bottom_row, bottom_col, left_row, left_col)


for T in range(int(input())):
    answer = 0xffffffff
    length = int(input())
    city = [list(map(int, input().split())) for _ in range(length)]
    copy_city = [[0] * length for _ in range(length)]
    cities = [0] * 5

    for r in range(length):
        for c in range(1, length - 1):
            for i in range(1, length):
                for j in range(1, length):
                    make_line(r, c, i, j)

    print(answer)