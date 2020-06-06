import sys
sys.stdin = open("5658.txt")

for T in range(int(input())):
    N, K = map(int, input().split())
    numbers = list(input())
    num = set()
    quat = N // 4

    for i in range(N):
        cnt = 1
        j = i
        temp = [''] * quat
        while cnt <= N:
            idx = cnt % quat
            temp[idx - 1] = numbers[j]
            j += 1
            cnt += 1

            if idx == 0:
                num.add(int("".join(temp), 16))
                temp = [''] * quat

            if j == N:
                j = 0

    num = sorted(list(num), reverse=True)

    print("#{} {}".format(T + 1, num[K - 1]))
