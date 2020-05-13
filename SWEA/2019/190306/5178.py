import sys
sys.stdin = open("5178.txt")

for t in range(int(input())):
    N, leaf, p = map(int, input().split())
    node = [0] * (N + 1)

    for _ in range(leaf):
        i, n = map(int, input().split())
        node[i] = n

    for i in range(N, -1, -1):
        node[i // 2] += node[i]

    print(f"#{t + 1} {node[p]}")