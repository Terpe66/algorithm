import sys
sys.stdin = open("2005.txt")

for t in range(int(input())):
    N = int(input())
    ans = [1]
    tmp = []
    print(f"#{t + 1}")
    for i in range(N):
        if i == 0:
            print(1)
            continue
        for a in range(i+1):
            if a == 0:
                print(1, end=" ")
                continue
            if a == i:
                print(1, end=" ")
                ans.append(1)
                continue
            new = ans[a-1] + ans[a]
            print(new, end=" ")
            tmp.append(new)
        for n in range(1, i):
            ans[n] = tmp.pop(0)
        print()