import sys
sys.stdin = open("14889.txt")


def get_point():
    global answer

    startPoint = 0
    linkPoint = 0

    for i in range(people):
        if check[i] == 1:
            for j in range(people):
                if check[j] == 1:
                    startPoint += team[i][j]

        elif check[i] == 0:
            for j in range(people):
                if check[j] == 0:
                    linkPoint += team[i][j]

    if answer > abs(startPoint - linkPoint):
        answer = abs(startPoint - linkPoint)


def get_start(idx, st):
    global answer

    if st == people // 2:
        get_point()
        return

    for i in range(idx, people):
        if check[i] == 0:
            check[i] = 1
            get_start(i + 1, st + 1)
            check[i] = 0


for T in range(int(input())):
    answer = 0xffffffff

    people = int(input())
    team = [list(map(int, input().split())) for _ in range(people)]
    check = [0] * people

    get_start(0, 0)

    print(answer)


