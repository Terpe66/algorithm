import sys
sys.stdin = open("5186.txt")

for t in range(int(input())):
    num = float(input())
    ans = ""
    while num > 0:
        num *= 2
        ans += str(num)[0]
        if num >= 1:
            num -= 1
        if len(str(num)) > 13:
            ans = "overflow"
            break

    print(f"#{t + 1} {ans}")