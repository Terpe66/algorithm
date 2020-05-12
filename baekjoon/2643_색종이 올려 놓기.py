import sys
sys.stdin = open("2643.txt")

N = int(input())
papers = []
for i in range(N):
    x, y = map(int, input().split())
    if x < y:
        papers.append((x, y))
        continue
    papers.append((y, x))
papers.sort()
print(papers)
ans = 1
for i in range(N - 1, 0, -1):
    j = i - 1
    while j > 0:
        if papers[i][1] >= papers[j][1] and papers[i][0] > papers[j][0]:
            ans += 1
            break
        j -= 1
print(ans)