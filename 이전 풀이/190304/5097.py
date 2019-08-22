from collections import deque
import sys
sys.stdin = open("5097.txt")

for t in range(int(input())):
    N, M = map(int, input().split())
    Q = deque(list(map(int, input().split())))

    for _ in range(M):
        Q.append(Q.popleft())

    print(f"#{t+1} {Q.popleft()}")