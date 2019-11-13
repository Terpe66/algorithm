import sys
sys.stdin = open("workshop.txt", "r")

for t in range(10):
    t = int(input())
    charlist = []
    for i in range(100):
        charlist.append(list(map(str, input().split())))
    
    ans = 1
    for i in range(100):
        start = 0
        idx = 100
        if ans == idx:
            break
        while start < 100:
            end = start + idx
            sublist = charlist[i][0][start:end]
            if sublist[::-1] == sublist and len(sublist) > ans :
                ans = len(sublist)
                break
            elif end == 100:
                start = 0
                idx -= 1
            else:
                start += 1

    charlist2 = []
    for c in range(100):
        charlist2.append([""])

    for i in range(100):
        for j in range(100):
            charlist2[i][0] += charlist[j][0][i]

    for i in range(100):
        start = 0
        idx = 100
        if ans == idx:
            break
        while start < 100:
            end = start + idx
            sublist = charlist2[i][0][start:end]
            if sublist[::-1] == sublist and len(sublist) > ans:
                ans = len(sublist)
                break
            elif end == 100:
                start = 0
                idx -= 1
            else:
                start += 1

    print("#{} {}".format(t+1, ans))

#1 18
#2 17
#3 17
#4 20
#5 18
#6 21
#7 18
#8 18
#9 17
#10 18


