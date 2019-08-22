import sys
sys.stdin = open("3347.txt")

for t in range(int(input())):
    Sports, Human = map(int, input().split())
    Money = list(map(int, input().split()))
    Max_money = list(map(int, input().split()))
    ans = [0] * (Sports + 1)
    half = int(Sports ** 0.5)
    while Max_money:
        m = Max_money.pop()
        for i in range(Sports):
            if Money[i] <= m:
                ans[i + 1] += 1
                break
        if ans[i + 1] >= half:
            break
    ans = ans.index(max(ans))
    print(f"#{t + 1} {ans}")