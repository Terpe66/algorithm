import sys
sys.stdin = open("2798.txt")

card, num = map(int, input().split())
cards = list(map(int, input().split()))
blackjack = 0
for i in range(1 << card):
    black = 0
    for j in range(card):
        if cards[j] > num:
            continue
        if black > num:
            break
        if black + cards[j] <= num and i & (1 << j) != 0:
            black += cards[j]

    if blackjack < black <= num:
        blackjack = black
        if blackjack == num:
            break

print(blackjack)