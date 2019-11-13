import sys
sys.stdin = open("3947.txt")

T = int(input())
for t in range(T):
    answer = 0
    B, R = map(int, input().split())

    MAP = [[] for _ in range(R + 1)]
    for i in range(R):
        start, end, pay = map(int, input().split())
        MAP[start].append((end, pay))
        MAP[end].append((start, pay))

    PAY = [1000000000 for _ in range(R + 1)]
    PAY[0] = 0
    for i in range(2, R + 1):
        PAY[i] *= i

    stack = []
    for i in range(len(MAP[1])):
        e, p = MAP[1][i]
        stack.append((e, p))
        PAY[e] = p

    visit = [False] * (R + 1)
    while stack:
        e, p = stack.pop()

        for i in range(len(MAP[e])):
            ne, np = MAP[e][i]
            if PAY[e] + np < PAY[ne]:
                stack.append((ne, np))
                PAY[ne] = np



    visit[0] = visit[1] = True
    stack = []
    for i in range(len(MAP[1])):
        s, e = MAP[1][i][0], MAP[1][i][1]
        stack.append((s, e))
        if visit[e] == False:
            visit[e] = True
            stack.append((s, e))
            answer += PAY[e]

    while stack:
        s, e = stack.pop()
        print("start", s, e)
        if s == B:
            break

        for i in range(len(MAP[e])):
            ns, ne = MAP[e][i][0], MAP[e][i][1]
            if visit[ne] == False:
                visit[ne] = True
                print("next", ns, ne)
                print(visit)
                stack.append((ns, ne))
                answer += PAY[ne]

    print("#{} {}".format(t + 1, answer))