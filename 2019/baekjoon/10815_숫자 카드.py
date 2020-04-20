import sys
sys.stdin = open("10815.txt")

N = int(input())
my_card = list(map(int, input().split()))
my_card.sort()
M = int(input())
nam_card = list(map(int, input().split()))
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
        print(1, end=" ")
    else:
        print(0, end=" ")
    i += 1

