import sys
sys.stdin = open("15686.txt")


def get_point(idx, count, M):
    global answer

    if count == M:
        if answer > sum(chickenCheck):
            answer = sum(chickenCheck)
        return

    for i in range(idx, len(chicken)):
        temp = [0] * len(house)
        for h in range(len(house)):
            new = abs(house[h][0] - chicken[i][0]) + abs(house[h][1] - chicken[i][1])
            if chickenCheck[h] > new:
                temp[h] = chickenCheck[h]
                chickenCheck[h] = new
        get_point(i + 1, count + 1, M)
        for h in range(len(house)):
            if temp[h]:
                chickenCheck[h] = temp[h]


for T in range(int(input())):
    answer = 0xffffffff
    length, M = map(int, input().split())
    board = []
    house = []
    chicken = []

    for i in range(length):
        inputs = input().split()
        for j in range(length):
            if inputs[j] == '1':
                house.append((i, j))
            elif inputs[j] == '2':
                chicken.append((i, j))
        board.append(inputs)

    chickenCheck = [0xffffffff] * len(house)
    get_point(0, 0, M)

    print(answer)