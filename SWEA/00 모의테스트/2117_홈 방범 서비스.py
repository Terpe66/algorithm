import sys
sys.stdin = open("2117.txt")


def home(row, col, k):
    global answer

    point = 0
    dis = k
    for r in range(row - k, row + 1):
        if r < 0 or r >= length:
            dis -= 1
            continue
        for c in range(col - k + dis, col + k + 1 - dis):
            if c < 0 or c >= length:
                continue
            if town[r][c] == 1:
                point += M
        dis -= 1

    dis = 1
    for r in range(row + 1, row + 1 + k):
        if r < 0 or r >= length:
            dis += 1
            continue
        for c in range(col - k + dis, col + k + 1 - dis):
            if c < 0 or c >= length:
                continue
            if town[r][c] == 1:
                point += M
        dis += 1

    if point >= pay:
        answer = max(answer, point)


for T in range(int(input())):
    answer = 0
    length, M = map(int, input().split())
    town = []

    max_point = 0
    for i in range(length):
        inputs = list(map(int, input().split()))
        for j in range(length):
            if inputs[j] == 1:
                max_point += M
        town.append(inputs)

    for k in range(length * 2, -1, -1):
        if answer:
            break
        pay = (k + 1) ** 2 + k ** 2
        if pay > max_point:
            continue
        for i in range(length):
            for j in range(length):
                home(i, j, k)

    print("#{} {}".format(T + 1, answer // M))
