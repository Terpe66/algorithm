import sys
sys.stdin = open("2383.txt")


def runaway(plist):
    global answer

    first = []
    second = []
    for i in range(person_length):
        if i in plist:
            first.append((distance[0][i], i))
        else:
            second.append((distance[1][i], i))
    first.sort()
    second.sort()

    ftmp = [0] * len(first)
    stair = office[stairs[0][0]][stairs[0][1]]
    for f in range(len(first)):
        if f < 3:
            ftmp[f] = first[f][0] + stair
        else:
            if ftmp[0] + 1 <= first[f][0]:
                ftmp[f] = first[f][0] + stair
            else:
                ftmp[f] = ftmp[f - 3] + stair

    stmp = [0] * len(second)
    stair = office[stairs[1][0]][stairs[1][1]]
    for s in range(len(second)):
        if s < 3:
            stmp[s] = second[s][0] + stair
        else:
            if stmp[0] + 1 <= second[s][0]:
                stmp[s] = second[s][0] + stair
            else:
                stmp[s] = stmp[s - 3] + stair

    if ftmp and stmp:
        answer = min(answer, max(max(ftmp), max(stmp)))
    elif ftmp and not stmp:
        answer = min(answer, max(ftmp))
    elif stmp and not ftmp:
        answer = min(answer, max(stmp))


def select_first(idx, now, deep, plist):

    if now == deep:
        runaway(plist)
        return

    for i in range(idx, person_length):
        select_first(i + 1, now + 1, deep, plist + [i])


for T in range(int(input())):
    length = int(input())
    answer = 0xffffffff
    office = []
    stairs = []
    person = []

    for i in range(length):
        inputs = list(map(int, input().split()))
        for j in range(length):
            if inputs[j] == 1:
                person.append((i, j))
            elif inputs[j] > 1:
                stairs.append((i, j))
        office.append(inputs)

    person_length = len(person)
    visit = [True] * person_length
    distance = [[0] * person_length for _ in range(2)]
    for i in range(2):
        for j in range(person_length):
            distance[i][j] = abs(stairs[i][0] - person[j][0]) + abs(stairs[i][1] - person[j][1])

    for i in range(person_length + 1):
        select_first(0, 0, i, [])

    print("#{} {}".format(T + 1, answer + 1))