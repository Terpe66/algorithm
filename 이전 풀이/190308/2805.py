import sys
sys.stdin = open("2805.txt")

for t in range(int(input())):
    size = int(input())

    farm = []
    for _ in range(size):
        farm.append(input())

    ans, cnt = 0, 0
    row, col = 0, size//2
    while row < size and col < size:
        if row <= col:
            for i in range(col-cnt, col+cnt+1):
                ans += int(farm[row][i])
            cnt += 1
            row += 1
            if row > col:
                cnt -= 2
        else:
            for i in range(col-cnt, col+cnt+1):
                ans += int(farm[row][i])
            cnt -= 1
            row += 1

    print(f"#{t+1} {ans}")