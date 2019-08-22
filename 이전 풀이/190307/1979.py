import sys
sys.stdin = open("1979.txt")

for t in range(int(input())):
    size, length = map(int, input().split())

    battle = []
    for _ in range(size):
        battle.append(input().split())

    ans = 0
    for row in range(size):
        for col in range(size):
            if battle[row][col] == "0":
                continue
            rcnt, ccnt, ridx, cidx = 1, 1, row, col
            if col:
                if battle[row][col-1] != "1":
                    while cidx+1 < size and battle[row][cidx+1] == "1" and ccnt < length+1:
                        ccnt += 1
                        cidx += 1
            else:
                while cidx+1 < size and battle[row][cidx+1] == "1" and ccnt < length+1:
                    ccnt += 1
                    cidx += 1

            if row:
                if battle[row-1][col] != "1":
                    while ridx+1 < size and battle[ridx+1][col] == "1" and rcnt < length+1:
                        rcnt += 1
                        ridx += 1
            else:
                while ridx+1 < size and battle[ridx+1][col] == "1" and rcnt < length+1:
                    rcnt += 1
                    ridx += 1

            if rcnt == length:
                ans += 1
            if ccnt == length:
                ans += 1

    print(f"#{t+1} {ans}")