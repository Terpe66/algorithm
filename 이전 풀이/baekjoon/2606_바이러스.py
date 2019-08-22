import sys
sys.stdin = open("2606.txt")

PC = int(input())
line = int(input())
net = [[] for _ in range(PC+1)]
for _ in range(line):
    n, w = map(int, input().split())
    net[n].append(w)
    net[w].append(n)

Q = [1]
visited = [False] * (PC + 1)
cnt = 0
while Q:
    idx = Q.pop()
    if visited[idx] == False:
        visited[idx] = True
        cnt += 1
    while net[idx]:
        Q.append(net[idx].pop(0))

print(cnt-1)