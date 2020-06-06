import sys
sys.stdin = open("1952.txt")


def lets_swim(idx, now):
    global answer

    if now > answer:
        return

    if idx >= 12:
        answer = min(answer, now)
        return

    lets_swim(idx + 3, now + pay[2])
    comp = month[idx] * pay[0]
    if comp < pay[1]:
        new = comp
    else:
        new = pay[1]
    i = 12
    for i in range(idx + 1, 12):
        if month[i]:
            break
    lets_swim(i, now + new)


for T in range(int(input())):
    pay = list(map(int, input().split()))
    month = list(map(int, input().split()))
    answer = min(pay[3], pay[2] * 4, pay[1] * 12, pay[0] * sum(pay))
    for i in range(12):
        if month[i]:
            lets_swim(i, 0)
            break

    print("#{} {}".format(T + 1, answer))
