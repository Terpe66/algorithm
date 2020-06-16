import sys
sys.stdin = open("1798.txt")


def lets_move(day, idx, now, left, lst):
    global answer, answer_list

    for i in range(N):
        if not visit[i]:
            if day == M:
                if point[i][0] == "P" and table[idx][i] + point[i][1] + table[i][0] <= left:
                    visit[i] = 1
                    lets_move(day, i, now + point[i][2], left - (table[idx][i] + point[i][1]), lst + [i])
                    visit[i] = 0
                elif day == M and i == N - 1:
                    if answer < now:
                        answer = now
                        answer_list = lst + [0]
                    return
            else:
                if point[i][0] == "P" and table[idx][i] + point[i][1] < left:
                    new = table[idx][i] + point[i][1]
                    for j in hotel:
                        if new + table[i][j] <= left:
                            break
                    else:
                        continue
                    visit[i] = 1
                    lets_move(day, i, now + point[i][2], left - new, lst + [i])
                    visit[i] = 0
                elif point[i][0] == "H" and table[idx][i] <= left:
                    lets_move(day + 1, i, now, 540, lst + [i])


for T in range(int(input())):
    answer = 0
    N, M = map(int, input().split())
    table = [[0xffffffff] * N for _ in range(N)]
    for i in range(N - 1):
        inputs = [0xffffffff] * (i + 1) + list(map(int, input().split()))
        for j in range(i + 1, N):
            table[i][j] = table[j][i] = inputs[j]

    hotel = []
    point = []
    for i in range(N):
        inputs = input().split()
        if len(inputs) > 1:
            point.append([inputs[0], int(inputs[1]), int(inputs[2])])
        else:
            point.append([inputs[0]])
            if inputs[0] == "H":
                hotel.append(i)

    visit = [0] * N
    answer_list = []
    lets_move(1, 0, 0, 540, [])

    print("#{} {}".format(T + 1, answer), end=" ")
    for i in answer_list:
        print(i + 1, end=" ")
    print()
