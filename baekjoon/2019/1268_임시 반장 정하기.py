import sys
sys.stdin = open("1268.txt")

N = int(input())
grade = [input().split() for _ in range(N)]

S = [[False] * N for _ in range(N)]

for idx in range(N):
    for row in range(5):
        for col in range(N):
            if idx != col and S[idx][col] == False and grade[idx][row] == grade[col][row]:
                S[idx][col] = True

ans = (0, 0)
for i in range(N):
    tmp = S[i].count(True)
    if ans[1] < tmp:
        ans = (i, tmp)

print(ans[0] + 1)
