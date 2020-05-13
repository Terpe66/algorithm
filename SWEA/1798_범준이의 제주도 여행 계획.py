import sys
sys.stdin = open("1798.txt")

for T in range(int(input())):
    answer = 0
    answerRoute = []
    point, day = map(int, input().split())

    island = [[0 * point for i in range(point)] for j in range(point)]
    for i in range(point - 1):
        inputs = input().split()
        for j in range(len(inputs)):
            island[i][j + i + 1] = int(inputs[j])
            island[j + i + 1][i] = int(inputs[j])

    move = []
    hotels = []
    pointInfo = []
    for i in range(point):
        inputs = input().split()
        if len(inputs) > 1:
            pointInfo.append((inputs[0], int(inputs[1]), int(inputs[2])))
            continue
        if inputs == ['A']:
            move.append((i, day - 1, 540, 0, []))
            airport = i
        if inputs == ['H']:
            hotels.append(i)
        pointInfo.append((inputs[0], 0, 0))

    while move:
        now, restDay, restTime, sati, visitList = move.pop()

        for i in range(point):
            if i in visitList and i not in hotels:
                continue
            if i == now:
                continue
            spendTime = island[now][i] + pointInfo[i][1]
            if restDay > 0:
                if restTime < spendTime:
                    continue
                if pointInfo[i][0] == 'A' and 0 < sati >= answer and pointInfo[now][0] == 'H':
                    answer = sati
                    answerRoute = visitList + [i]
                elif pointInfo[i][0] == 'P':
                    for h in hotels:
                        if restTime >= spendTime + island[i][h]:
                            move.append((i, restDay, restTime - spendTime, sati + pointInfo[i][2], visitList + [i]))
                            break
                elif pointInfo[i][0] == 'H' and sati > 0:
                    move.append((i, restDay - 1, 540, sati, visitList + [i]))
            elif restDay == 0:
                if i != airport and restTime < spendTime + island[i][airport]:
                    continue
                if i == airport and restTime < spendTime:
                    continue
                if pointInfo[i][0] == 'A' and 0 < sati >= answer:
                    answer = sati
                    answerRoute = visitList + [i]
                elif pointInfo[i][0] == 'P':
                    move.append((i, 0, restTime - spendTime, sati + pointInfo[i][2], visitList + [i]))


    print("#{} {}".format(T + 1, answer), end=" ")

    for i in range(len(answerRoute)):
        print(answerRoute[i] + 1, end=" ")
    print()