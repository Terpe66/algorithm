import sys
sys.stdin = open("4789.txt")

for t in range(int(input())):
    P = list(map(int, input()))
    length = len(P)
    ans = 0
    clap = 0
    for i in range(length):
        if i - 1 >= 0 and P[i] and P[i - 1] == 0:
            if clap < i:
                ans += i - clap
                clap += i - clap
        if P[i]:
            clap += P[i]
        i += 1

    print(f"#{t + 1} {ans}")