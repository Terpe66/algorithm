from collections import deque

import sys
sys.stdin = open("2477.txt")


for T in range(int(input())):
    answer = 0
    info_length, repair_length, person_num, info_num, repair_num = map(int, input().split())
    person_data = [[0, 0] for _ in range(person_num)]
    info = list(map(int, input().split()))
    repair = list(map(int, input().split()))
    arrive = list(map(int, input().split()))
    info_now = [0] * info_length
    repair_now = [0] * repair_length

    t = arrive[0]
    wait = [deque(), []]
    start = 0
    temp = []
    while True:
        # print("#{} 시간: {}".format(T + 1, t))
        for i in range(start, person_num):
            if -1 < arrive[i] <= t:
                wait[0].append(i)
                arrive[i] = -1
                start = i + 1
            else:
                break

        if wait[1]:
            wait[1] = sorted(wait[1], key=lambda x: x[1])
            for i in range(len(wait[1])):
                n, idx = wait[1][i]
                if info_now[idx] == 0:
                    temp.append((n, idx))
            for i in range(len(wait[1]) - 1, -1, -1):
                if wait[1][i] in temp:
                    wait[1].pop(i)

        if temp:
            for i in range(repair_length):
                if not temp:
                    break
                if repair_now[i] == 0:
                    repair_now[i] = repair[i]
                    pidx, trsh = temp.pop(0)
                    person_data[pidx][1] = i + 1

        if wait[0]:
            for i in range(info_length):
                if not wait[0]:
                    break
                if info_now[i] == 0:
                    info_now[i] = info[i]
                    pidx = wait[0].popleft()
                    wait[1].append((pidx, i))
                    person_data[pidx][0] = i + 1

        for i in range(info_length):
            if info_now[i] > 0:
                info_now[i] -= 1

        for i in range(repair_length):
            if repair_now[i] > 0:
                repair_now[i] -= 1

        if start == person_num and not wait[0] and not wait[1] and not temp:
            break

        t += 1

    for i in range(person_num):
        if person_data[i] == [info_num, repair_num]:
            answer += i + 1

    if answer == 0:
        answer = -1
    print("#{} {}".format(T + 1, answer))
