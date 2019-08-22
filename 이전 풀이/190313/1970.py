import sys
sys.stdin = open("1970.txt")

for t in range(int(input())):
    price = int(input())
    money = [0] * 8

    for i in range(8):
        if i == 0:
            div = 50000

        if i == 1:
            div = 10000

        if i == 2:
            div = 5000

        if i == 3:
            div = 1000

        if i == 4:
            div = 500

        if i == 5:
            div = 100

        if i == 6:
            div = 50

        if i == 7:
            div = 10

        minus = price // div
        money[i] = minus
        price -= minus * div

    print(f"#{t+1}")
    for i in range(8):
        print(money[i], end=" ")
    print()