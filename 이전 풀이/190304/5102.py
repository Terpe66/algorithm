import sys
sys.stdin = open("5102.txt")

for t in range(int(input())):
    Node, Line = map(int, input().split())
    node = [[] for _ in range(Node+1)]
    for _ in range(Line):
        s, g = map(int, input().split())
        node[s].append(g)
        node[g].append(s)
    count = [-1] * (Node+1)
    start, goal = map(int, input().split())
    for i in range(1, Node+1):
        if start in node[i]:
            node[i].remove(start)

    Q = []
    cnt, ans = 0, -1
    count[start] = cnt
    Q.append(node[start])
    while Q:
        cnt += 1
        for i in Q.pop(0):
            if i == goal:
                if ans == -1:
                    ans = cnt
                elif ans > cnt:
                    ans = cnt
            elif node[i]:
                Q.append(node[i])
                node[i] = []


    print(f"#{t+1} {ans}")