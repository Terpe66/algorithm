import sys
sys.stdin = open("2193.txt")

N = int(input())
arr = [0] * (N + 1)
if N == 1:
    arr[1] = 1
if N >= 2:
    arr[1] = arr[2] = 1

i, j = 1, 2
while j + 1 <= N:
    arr[j + 1] = arr[i] + arr[j]
    i += 1
    j += 1

print(arr[N])