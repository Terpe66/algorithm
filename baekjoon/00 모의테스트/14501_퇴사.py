import sys
sys.stdin = open("14501.txt")


def adv(day, money):
    global answer

    if day == last:
        if answer < money:
            answer = money
        return

    for d in range(day, last):
        if d + schedule[d][0] <= last:
            adv(d + schedule[d][0], money + schedule[d][1])
    else:
        adv(last, money)



for T in range(int(input())):
    answer = 0
    last = int(input())
    schedule = [tuple(map(int, input().split())) for _ in range(last)]

    adv(0, 0)

    print(answer)