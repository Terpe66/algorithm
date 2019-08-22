import sys
sys.stdin = open("1463.txt")

N = int(input())
c = [0, 0] + [1000000] * (N - 1)
for i in range(2, N + 1):
    c[i] = c[i-1] + 1
    if i % 2 == 0:
        c[i] = min(c[i], c[i//2] + 1)
    if i % 3 == 0:
        c[i] = min(c[i], c[i//3] + 1)
print(c[N])

