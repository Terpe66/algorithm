import sys
sys.stdin = open("5122.txt")

for t in range(int(input())):
    suyul, coin, print_index = map(int, input().split())
    base = input().split()
    req = []
    for _ in range(coin):
        req.append(input().split())

    cnt = len(base)
    for i in range(cnt):
        base.append([i, base.pop(0)])

    while req:
        pop = req.pop(0)
        do, idx = pop.pop(0), int(pop.pop(0))
        if do != "D":
            new = pop.pop(0)

        length = len(base)
        if do == "I":
            for i in range(length):
                if base[i][0] >= idx:
                    base[i][0] += 1

            base.append([idx, new])

        elif do == "D":
            for i in range(length):
                if base[i][0] == idx:
                    base[i] = [-1, "X"]

            for i in range(length):
                if base[i][0] > idx:
                    base[i][0] -= 1

        elif do == "C":
            for i in range(length):
                if base[i][0] == idx:
                    base[i][1] = new

    for i in range(length):
        if base[i][0] == print_index:
            print(f"#{t+1} {base[i][1]}")
            break
    else:
        print(f"#{t+1} -1")
