import sys
sys.stdin = open("10816.txt")

N = int(input())
my_card = list(map(int, input().split()))
my_card.sort()
M = int(input())
nam_card = list(map(int, input().split()))
cnt_dict = {}
i = 0
while i < N:
    n = my_card[i]
    if n not in cnt_dict:
        cnt_dict[n] = 1
    else:
        cnt_dict[n] += 1
    i += 1

i = 0
while i < M:
    l, r = 0, N - 1
    mid = (l + r) // 2
    while l != r and nam_card[i] != my_card[mid]:
        if nam_card[i] < my_card[mid]:
            r = mid
            mid = (l + r) // 2
        elif nam_card[i] >= my_card[mid]:
            l = mid + 1
            mid = (l + r) // 2
    if my_card[mid] == nam_card[i]:
        print(cnt_dict[my_card[mid]], end=" ")
    else:
        print(0, end=" ")
    i += 1
