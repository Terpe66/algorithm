import sys
sys.stdin = open("4869.txt")

for t in range(int(input())):
    tape = int(input())
    rectangle = [0] * (tape//10)


def DFS(start):


    global result
    visit[start] = True
    for m in G[start]:
        if m == end:
            result = 1
            break
        elif not visit[m]: # False인지 보기
            DFS(m)

for t in range(int(input())):
    V, E = map(int, input().split())
    G = [[] for v in range(V + 1)]

    for _ in range(E):
        s, e = map(int, input().split())
        G[s].append(e)

    visit = [False for _ in range(V + 1)]
    start, end = map(int, input().split())
    result = 0

    DFS(start)
    print(f"#{t+1} {result}")