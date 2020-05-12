import sys
sys.stdin = open("workshop.txt")

for t in range(10):
    V, E = map(int, input().split())
    S = []
    ans = []
    G = [[] for _ in range(V + 1)]
    visit = [0] * (V + 1)
    g = list(map(int, input().split()))
    for i in range(0, len(g), 2):
        G[g[i]].append(g[i+1])
        visit[g[i+1]] += 1

    nodes = [i for i in range(1, V + 1)]
    start, cnt = 1, V
    print(f"#{t + 1}", end=" ")
    while cnt > 0:
        for i in nodes:
            if visit[i] == 0:
                break
        S.append(i)

        while S:
            t = S.pop()
            ans.append(t)
            nodes.remove(t)
            cnt -= 1
            for e in G[t]:
                visit[e] -= 1
                if visit[e] == 0:
                    S.append(e)

    for i in ans:
        print(i, end=" ")
    print()