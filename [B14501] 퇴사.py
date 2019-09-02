import sys
sys.stdin = open("B14501.txt")

def get_money(sche, money):
    global ans

    if sche == day:
        if ans < money:
            ans = money
        return

    i = sche
    while i < day:
        if schedule[i] == False:
            idx = i
            max_idx = i + consulting[i][0]
            if max_idx >= day + 1:
                while idx < day:
                    schedule[idx] = True
                    idx += 1
                get_money(idx, money)
                idx = i
                while idx < day:
                    schedule[idx] = False
                    idx += 1
            else:
                while idx < max_idx:
                    schedule[idx] = True
                    idx += 1
                get_money(idx, money + consulting[i][1])
                idx = i
                while idx < max_idx:
                    schedule[idx] = False
                    idx += 1
        i += 1


for t in range(int(input())):

    day = int(input())
    consulting = [list(map(int, input().split())) for _ in range(day)]

    schedule = [False] * day
    ans = 0

    get_money(0, 0)

    print(ans)