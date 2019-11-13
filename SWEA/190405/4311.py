import sys
sys.stdin = open("4311.txt")

for t in range(int(input())):
    N, O, C = map(int, input().split())
    nums = list(map(int, input().split()))
    calc = input().split()
    target = int(input())
    tnum = str(target)
    target_chk = [False] * len(tnum)
    ans = 1


    i = 0
    while i < len(tnum):
        if int(tnum[i]) in nums:
            tnum = tnum[:i] + tnum[i + 1:]
            ans += 1
        else:
            i += 1
    if not tnum:
        print(f"#{t + 1} {ans - 1}")
        continue

    print(f"#{t + 1} {ans}")