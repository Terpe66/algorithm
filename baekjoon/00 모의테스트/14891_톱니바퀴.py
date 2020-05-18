import sys
sys.stdin = open("14891.txt")


def turn_wheels(idx, dir, l, r):
    # 2, 6
    ldx, rdx = 6, 2
    if dir == 1:
        ldx += 1
        rdx += 1
        temp = wheels[idx][7]
        for i in range(7, 0, -1):
            wheels[idx][i] = wheels[idx][i - 1]
        wheels[idx][0] = temp
    elif dir == -1:
        ldx -= 1
        rdx -= 1
        temp = wheels[idx][0]
        for i in range(7):
            wheels[idx][i] = wheels[idx][i + 1]
        wheels[idx][7] = temp

    if idx == 0:
        if r == 0 and wheels[idx][rdx] != wheels[idx + 1][6]:
            turn_wheels(idx + 1, dir * -1, 1, 0)
    elif idx == 3:
        if l == 0 and wheels[idx][ldx] != wheels[idx - 1][2]:
            turn_wheels(idx - 1, dir * - 1, 0, 1)
    else:
        if l == 0 and wheels[idx][ldx] != wheels[idx - 1][2]:
            turn_wheels(idx - 1, dir * -1, 0, 1)
        if r == 0 and wheels[idx][rdx] != wheels[idx + 1][6]:
            turn_wheels(idx + 1, dir * -1, 1, 0)


for T in range(int(input())):
    answer = 0
    wheels = [[0] * 8 for _ in range(4)]
    for i in range(4):
        inputs = input()
        for j in range(8):
            wheels[i][j] = inputs[j]

    turn = int(input())
    cmd = [tuple(map(int, input().split())) for _ in range(turn)]

    for idx, dir in cmd:
        turn_wheels(idx - 1, dir, 0, 0)

    for i in range(4):
        if wheels[i][0] == '1':
            answer += 2 ** i


    print(answer)