from collections import deque
import sys
sys.stdin = open("5099.txt")

for t in range(int(input())):
    N, M = map(int, input().split())
    oven = deque([])
    pizza = deque(list(map(int, input().split())))

    for p in range(M):
        pizza[p] = [p+1, pizza[p]]

    while True:
        while len(oven) < N and pizza:
            oven.appendleft(pizza.popleft())
        while oven[0][1] > 0:
            oven.rotate(1)
            oven[0][1] //= 2
        if oven[0][1] == 0:
            oven.popleft()
        if len(oven) == 1:
            print(f"#{t+1} {oven[0][0]}")
            break

