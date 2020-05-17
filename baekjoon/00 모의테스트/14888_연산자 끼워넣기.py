import sys
sys.stdin = open("14888.txt")


def calc(idx, num):
    global maxNum, minNum

    if idx + 1 == len(numbers):
        if maxNum < num:
            maxNum = num
        if minNum > num:
            minNum = num
        return

    for i in range(4):
        if sign[i] > 0:
            sign[i] -= 1
            if i == 0:
                new = num + numbers[idx + 1]
            elif i == 1:
                new = num - numbers[idx + 1]
            elif i == 2:
                new = num * numbers[idx + 1]
            elif i == 3:
                new = abs(num) // numbers[idx + 1]
                if num < 0:
                    new *= -1
            calc(idx + 1, new)
            sign[i] += 1


for T in range(int(input())):
    maxNum = -0xffffffff
    minNum = 0xffffffff
    N = int(input())
    numbers = list(map(int, input().split()))
    sign = list(map(int, input().split()))

    calc(0, numbers[0])

    print(maxNum)
    print(minNum)