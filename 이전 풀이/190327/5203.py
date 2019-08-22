import sys
sys.stdin = open("5203.txt")

for t in range(int(input())):
    p1 = [0] * 10
    p2 = [0] * 10
    tmp = input().split()

    ans = 0
    for n in range(12):
        idx = int(tmp[n])
        if n % 2:
            p2[idx] += 1
        else:
            p1[idx] += 1

        if n > 5:
            if p1[idx] == 3:
                ans = 1
                break
            if p2[idx] == 3:
                ans = 2
                break

            if idx <= 1:
                if p1[idx] and p1[idx + 1] and p1[idx + 2]:
                    ans = 1
                    break
                if p2[idx] and p2[idx + 1] and p2[idx + 2]:
                    ans = 2
                    break

            elif idx >= 8:
                if p1[idx] and p1[idx - 1] and p1[idx - 2]:
                    ans = 1
                    break
                if p2[idx] and p2[idx - 1] and p2[idx - 2]:
                    ans = 2
                    break

            else:
                i = 0
                while i < 3:
                    if p1[idx + i] and p1[idx + i - 1] and p1[idx + i - 2]:
                        ans = 1
                        break
                    if p2[idx + i] and p2[idx + i - 1] and p2[idx + i - 2]:
                        ans = 2
                        break
                    i += 1
                if ans:
                    break

    print(f"#{t + 1} {ans}")