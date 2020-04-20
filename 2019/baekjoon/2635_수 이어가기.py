import sys
sys.stdin = open("2635.txt")

N = int(input())
# while N <= 30000:
if N <= 2:
    n = N - 1
else:
    n = N // 2
max_cnt = 0
while 0 <= n <= N:
    LIST = [N, n]
    i = 1
    while LIST[i - 1] >= LIST[i]:
        LIST.append(LIST[i - 1] - LIST[i])
        i += 1
    if len(LIST) < max_cnt:
        break
    max_cnt = len(LIST)
    ans = LIST[:]
    n += 1
print(max_cnt)
for a in ans:
    print(a, end=" ")
print()