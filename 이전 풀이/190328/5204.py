import sys
sys.stdin = open("5204.txt")

def div(LIST):
    global ans
    length = len(LIST)
    idx = length // 2
    l1 = LIST[:idx]
    l2 = LIST[idx:]

    if len(l1) > 1:
        l1 = div(l1)
    if len(l2) > 1:
        l2 = div(l2)

    if l1[-1] > l2[-1]:
        ans += 1
        return l2 + l1
    else:
        return l1 + l2

for t in range(int(input())):
    N = int(input())
    num_list = list(map(int, input().split()))
    ans = 0
    tmp = div(num_list)

    num_list.sort()
    n = num_list[N//2]

    print(f"#{t + 1} {ans} {n}")