import sys
sys.stdin = open("2458.txt")

ch, line = map(int, input().split())
key = [[] for _ in range(ch + 1)]
ans = [0] * (ch + 1)
for _ in range(line):
    x, y = map(int, input().split())
    key[x].append(y)

for i in range(1, ch + 1):
    if key[i]:
        S = [i]
        A = [True] * (ch + 1)
        while S:
            pop = S.pop()
            if A[pop]:
                A.append(pop)
            for k in range(len(key[pop])):
                new = key[pop][k]
                if A[new]:
                    S.append(new)
                    A[new] = False
                    ans[i] += 1
                    ans[new] += 1

print(ans.count(ch-1))