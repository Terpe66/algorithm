import sys
sys.stdin = open("4613.txt")

for t in range(int(input())):
    height, width = map(int, input().split())

    flag = []
    ans = 0
    for _ in range(height):
        if _ == 0 or _ == height - 1:
            f = input()
            i = 0
            while i < width:
                if _ == 0 and f[i] != "W":
                    ans += 1
                elif _ == height - 1 and f[i] != "R":
                    ans += 1
                i += 1
        else:
            flag.append(input())

    length = height - 2
    empty = []
    i, j = 1, 0
    while i < length + 1 and j < length:
        empty.append((length - i, length - (length - i) - j, length - (length - i) - (length - (length - i) - j)))
        j += 1
        if i == j:
            j = 0
            i += 1

    chk = ("W", "B", "R")
    old = length * width
    for color in empty:
        new = j = 0
        for i in range(color[0]):
            while j < width:
                if flag[i][j] != chk[0]:
                    new += 1
                j += 1
            j = 0
        for i in range(color[0], color[0] + color[1]):
            while j < width:
                if flag[i][j] != chk[1]:
                    new += 1
                j += 1
            j = 0
        for i in range(color[0] + color[1], sum(color)):
            while j < width:
                if flag[i][j] != chk[2]:
                    new += 1
                j += 1
            j = 0
        if old > new:
            old = new

    ans += old
    print(f"#{t + 1} {ans}")