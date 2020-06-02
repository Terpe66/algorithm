import sys
sys.stdin = open("4013.txt")


def turn_mag(idx, d, l, r):

    left, right = mag[idx][6], mag[idx][2]
    if d == 1:
        temp = mag[idx][7]
        for i in range(7, 0, -1):
            mag[idx][i] = mag[idx][i - 1]
        mag[idx][0] = temp
    else:
        temp = mag[idx][0]
        for i in range(7):
            mag[idx][i] = mag[idx][i + 1]
        mag[idx][7] = temp

    if l == 0 and 0 <= idx - 1 < 4 and mag[idx - 1][2] != left:
        turn_mag(idx - 1, d * -1, 0, 1)
    if r == 0 and 0 <= idx + 1 < 4 and mag[idx + 1][6] != right:
        turn_mag(idx + 1, d * -1, 1, 0)


for T in range(int(input())):
    answer = 0
    K = int(input())
    mag = [list(map(int, input().split())) for _ in range(4)]
    turns = [list(map(int, input().split())) for _ in range(K)]

    for idx, d in turns:
        turn_mag(idx - 1, d, 0, 0)

    for i in range(4):
        if mag[i][0] == 1:
            answer += 2 ** i

    print("#{} {}".format(T + 1, answer))