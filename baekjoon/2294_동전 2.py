import sys
sys.stdin = open("2294.txt")

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
# coins.sort()
c = [0] + [1000000] * k
for coin in coins:
    for j in range(coin, k + 1):
        c[j] = min(c[j], c[j - coin] + 1)

if c[k]:
    print(c[k])
else:
    print(-1)