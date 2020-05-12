import sys
sys.stdin = open("B17281.txt")


def find_order(idx):
    if idx == 9:
        add_point()
        return

    before = None
    for i in range(9):

        if not play_check[i]:
            if idx == 3:
                find_order(idx + 1)
            else:
                play_check[i] = True
                play_order[idx] = i
                find_order(idx + 1)
                play_check[i] = False


def add_point():
    global ans

    inni = 0
    i = 0
    out = 0
    point_list = [0] * 4
    point = 0
    while inni < inning:
        idx = play_order[i]
        if players[inni][idx] == 0:
            out += 1
        else:
            p = players[inni][idx]

            for idx, po in enumerate(point_list):
                point_list[idx] += p
                if point_list[idx] >= 4:
                    point += 4
                    point_list[idx] = 0

            cnt = point_list.count(0)
            while cnt > 0:
                for idx in range(1, 4):
                    point_list[idx - 1] = point_list[idx]
                    point_list[idx] = 0

        if out == 3:
            inni += 1
            out = 0
            point_list = []

        i += 1
        if i == 9:
            i = 0

    if ans < point:
        ans = point
    return


for t in range(int(input())):
    inning = int(input())
    players = [list(map(int, input().split())) for _ in range(inning)]
    for i in range(inning):
        players[i][0], players[i][3] = players[i][3], players[i][0]

    play_check = [False] * 9
    play_check[3] = True
    play_order = [10] * 9
    play_order[3] = 3
    ans = 0

    find_order(0)
    print(ans // 4)
