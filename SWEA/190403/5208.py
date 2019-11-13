import sys
sys.stdin = open("5208.txt")

for t in range(int(input())):
    N = input().split()
    LIST = []
    for i in range(len(N)):
        if i > 0:
            LIST.append(int(N[i]))
    N = int(N[0])

    temp, tmp = [], 0
    while i > 0:
        j = i - 1
        while j >= 0:
            if LIST[j] >= i - j:
                tmp = j
            j -= 1
        temp.append(tmp)
        i = tmp

    print(f"#{t + 1} {len(temp) - 1}")