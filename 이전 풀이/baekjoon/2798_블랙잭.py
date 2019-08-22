import sys
sys.stdin = open("2978.txt")

def black(i, n, sum_num=0):
    global num, max_num, card
    n -= 1
    sum_num += cards[i]
    if sum_num > num or max_num == num:
        return

    if n == 0 and sum_num <= num:
        if sum_num > max_num:
            max_num = sum_num
            return

    if n > 0:
        while i + 1 < card:
            black(i + 1, n, sum_num)
            i += 1


card, num = map(int, input().split())
cards = list(map(int, input().split()))
max_num = 0

for i in range(card):
    black(i, 3)

print(max_num)