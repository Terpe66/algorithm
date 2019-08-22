import sys
sys.stdin = open("5644.txt")

for t in range(int(input())):
    move, cp = map(int, input().split())
    person_1 = [""] + input().split()
    person_2 = [""] + input().split()

    charge = [tuple(map(int, input().split())) for _ in range(cp)]
    charge_spot = [[] for _ in range(cp)]
    for i in range(cp):
        col, row, rng, per = charge[i]

        c = 0
        for j in range(row - rng, row + rng + 1):
            for k in range(col - c, col + c + 1):
                if 0 < j <= 10 and 0 < k <= 10:
                    charge_spot[i].append((j, k))
            if j < row:
                c += 1
            else:
                c -= 1


    chk = 0
    while chk < 2:
        if chk == 0:
            row = col = 1
            tmp = person_1
        elif chk == 1:
            row = col = 10
            tmp = person_2


        for i in range(move + 1):
            if tmp[i] == "1":
                row -= 1
            elif tmp[i] == "2":
                col += 1
            elif tmp[i] == "3":
                row += 1
            elif tmp[i] == "4":
                col -= 1

            tmp[i] = []
            for j in range(cp):
                if (row, col) in charge_spot[j]:
                    tmp[i].append((charge[j][3], j))
        chk += 1

    ans = 0
    for i in range(move + 1):
        if not person_1[i] and not person_2[i]:
            continue
        if len(person_1[i]) == 1 and len(person_2[i]) == 1:
            if person_1[i] == person_2[i]:
                ans += person_1[i][0][0]
            else:
                ans += person_1[i][0][0] + person_2[i][0][0]
        elif len(person_1[i]) == 1 and not person_2[i]:
            ans += person_1[i][0][0]
        elif len(person_2[i]) == 1 and not person_1[i]:
            ans += person_2[i][0][0]
        elif len(person_1[i]) > 1 and not person_2[i]:
            ans += max(person_1[i])[0]
        elif len(person_2[i]) > 1 and not person_1[i]:
            ans += max(person_2[i])[0]
        else:
            if max(person_1[i]) == max(person_2[i]):
                base = max(person_1[i])
                a = b = (0, 0)
                for j in range(len(person_1[i])):
                    if a < person_1[i][j] != base:
                        a = person_1[i][j]
                for j in range(len(person_2[i])):
                    if b < person_2[i][j] != base:
                        b = person_2[i][j]
                tmp = max(a, b)
                if base[0] // 2 > base[0] + tmp[0]:
                    ans += base[0]
                else:
                    ans += base[0] + tmp[0]
            else:
                ans += max(person_1[i])[0] + max(person_2[i])[0]

    print(f"#{t + 1} {ans}")