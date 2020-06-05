import sys
sys.stdin = open("4008.txt")


def calc(idx, now):
    global max_num, min_num

    if idx == N - 1:
        max_num = max(max_num, now)
        min_num = min(min_num, now)
        return

    for i in range(4):
        if calc_list[i]:
            calc_list[i] -= 1
            if i == 0:
                calc(idx + 1, now + number[idx + 1])
            elif i == 1:
                calc(idx + 1, now - number[idx + 1])
            elif i == 2:
                calc(idx + 1, now * number[idx + 1])
            elif i == 3:
                if now < 0:
                    calc(idx + 1, abs(now) // number[idx + 1] * - 1)
                else:
                    calc(idx + 1, now // number[idx + 1])
            calc_list[i] += 1


for T in range(int(input())):
    max_num = -0xffffffff
    min_num = 0xffffffff
    N = int(input())
    calc_list = list(map(int, input().split()))
    number = list(map(int, input().split()))
    calc(0, number[0])

    print("#{} {}".format(T + 1, max_num - min_num))
