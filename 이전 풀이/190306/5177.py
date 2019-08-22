import sys
sys.stdin = open("5177.txt")

for t in range(int(input())):
    N = int(input())
    inputs = [0]
    inputs += list(map(int, input().split()))

    idx = 0
    while idx < N + 1:
        if inputs[idx] < inputs[idx // 2]:
            inputs[idx], inputs[idx // 2] = inputs[idx // 2], inputs[idx]
            idx //= 2
        else:
            idx += 1

    idx, ans = N, 0
    while idx > 0:
        idx //= 2
        ans += inputs[idx]

    print(f"#{t + 1} {ans}")