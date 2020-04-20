import sys
sys.stdin = open("5162.txt")

for t in range(int(input())):
    A, B, C = map(int, input().split())
    ans = 0
    if A < B:
        ans = C // A
        C -= ans * A
        ans += C // B
        print(f"#{t+1} {ans}")
        continue
    ans = C // B
    C -= ans * B
    ans += C // A
    print(f"#{t+1} {ans}")