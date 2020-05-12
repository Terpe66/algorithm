import sys
sys.stdin = open("8016.txt")
#
# 00 00   1
# 02 06   3 5 7
# 06 10   9 11 13 15 17
# 10 14   19 21 23 25 27 29 31
# 14 18   33 35 37 39 41 43 45 47 49
# 18 22   51 53 55 57 59 61 63 65 67 69 71

T = int(input())
for t in range(T):
    floor = int(input())

    if floor == 1:
        print("#{} {} {}".format(t + 1, 1, 1))
        continue

    if floor >= 2:
        l, r = 2, 6
        left, right = l + 1, r + 1

        while floor > 2:
            r += 4
            l += 4

            left += l
            right += r

            floor -= 1

    print("#{} {} {}".format(t + 1, left, right))
