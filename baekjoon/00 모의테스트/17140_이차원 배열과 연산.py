import sys
sys.stdin = open("17140.txt")


def calc_C(R, C, cur):

    temp_list = [[] for _ in range(C)]
    temp = 0
    for c in range(C):
        temp_dict = {}
        for r in range(R):
            if board[cur][r][c]:
                if temp_dict.get(board[cur][r][c], False):
                    temp_dict[board[cur][r][c]] += 1
                else:
                    temp_dict[board[cur][r][c]] = 1
        for k, v in temp_dict.items():
            temp_list[c].append((v, k))
        temp_list[c] = sorted(temp_list[c])[:100]
        if temp < len(temp_list[c]) * 2:
            temp = len(temp_list[c]) * 2

    if temp > 100:
        temp = 100

    return temp_list, temp


def calc_R(R, C, cur):

    temp_list = [[] for _ in range(R)]
    temp = 0
    for i, r in enumerate(board[cur][:100]):
        temp_dict = {}
        for c in r:
            if c:
                if temp_dict.get(c, False):
                    temp_dict[c] += 1
                else:
                    temp_dict[c] = 1
        for k, v in temp_dict.items():
            temp_list[i].append((v, k))
        temp_list[i] = sorted(temp_list[i])[:100]
        if temp < len(temp_list[i]) * 2:
            temp = len(temp_list[i]) * 2

    if temp > 100:
        temp = 100

    return temp_list, temp


for T in range(int(input())):
    row, col, target = map(int, input().split())
    board = [[list(map(int, input().split())) for _ in range(3)], [[] for _ in range(3)]]
    row -= 1
    col -= 1

    answer = 0
    R = C = 3
    cur = 0
    while True:
        next = (cur + 1) % 2

        if 0 <= row < R and 0 <= col < C and board[cur][row][col] == target:
            break

        if R >= C:
            calc_list, temp_c = calc_R(R, C, cur)
            if len(board[next]) <= R:
                for _ in range(R - len(board[next])):
                    board[next].append([])
            else:
                for _ in range(R - len(board[next])):
                    board[next].pop()

            for i, list_row in enumerate(calc_list):
                temp = []
                for v, k in list_row:
                    temp += [k, v]
                board[next][i] = temp + [0] * (temp_c - len(temp))
            C = temp_c
            R = len(calc_list)
        else:
            calc_list, temp_c = calc_C(R, C, cur)
            for i in range(len(board[next])):
                board[next][i][:len(calc_list)] += [0] * (len(calc_list) - len(board[next][i]))

            if len(board[next]) <= len(calc_list):
                for _ in range(temp_c - len(board[next])):
                    board[next].append([0] * len(calc_list))
            else:
                for _ in range(temp_c - len(board[next])):
                    board[next].pop()

            for i, list_row in enumerate(calc_list):
                temp = []
                for v, k in list_row:
                    temp += [k, v]
                temp += [0] * (temp_c - len(temp))
                for j in range(len(temp)):
                    board[next][j][i] = temp[j]

            C = len(calc_list)
            R = temp_c

        cur = next
        answer += 1

        if answer > 100:
            answer = -1
            break


    print(answer)