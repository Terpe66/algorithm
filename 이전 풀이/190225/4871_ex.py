import sys
sys.stdin = open("4871.txt")


# 재귀 함수를 만듭니다.
def DFS(start):
    global result
    # 시작 지점의 방문 기록을 해줍니다.
    visit[start] = True
    # 그래프의 간선 시작(index)과 연결된 곳이 많을 수 있기 때문에 for문으로 확인합니다
    for m in G[start]:
        # 연결된 곳(간선 끝)이 끝(end)과 같으면 시작에서 끝까지 갈 수 있기 때문에 result는 1이 됩니다
        if m == end:
            result = 1
            break
        # 연결된 곳(간선 끝)이 끝(end)과 다를 경우, 간선 끝이 방문했던 곳이면 패스,
        # 방문했던 곳이 아니면 다시 함수로 접근해서
        # 그 간선 끝지점이 시작점이 되어, 연결된 노드가 있는지 확인합니다
        elif not visit[m]: # False인지 보기
            DFS(m)


for t in range(int(input())):
    # 노드(V), 간선(E) = map(int, input().split())
    V, E = map(int, input().split())
    # 그래프(G) = [ [] for _ in range(노드 + 1)] => 노드가 1번부터 있기 때문에 0번은 공란으로 둡니다.
    G = [ [] for _ in range(V + 1)]

    # 그래프에 간선의 시작과 끝 정보를 담아줍니다
    for _ in range(E):
        # 간선 시작(s), 간선 끝(e) = map(int, input().split())
        s, e = map(int, input().split())
        # 그래프[시작].append(끝) => 그래프의 시작 index에 연결된 노드의 끝 번호를 append 해줍니다
        G[s].append(e)
        # 만약 양방향 노드로 생각해야 할 때는
        # 그래프(G)[끝(e)].append(시작(s)

    # 방문 정보를 기록하기 위해 그래프와 같이 visit list를 생성해줍니다
    visit = [False for _ in range(V + 1)]
    # 모든 그래프의 구성이 완료되고, 그래프의 시작과 끝을 입력받습니다
    start, end = map(int, input().split())
    result = 0

    # DFS(start)

    # 스택을 만듭니다
    stack = []
    # 노드의 시작을 스택에 넣어줍니다
    stack.append(start)
    # 시작을 방문처리 해줍니다
    visit[start] = True
    # 스택이 비어있지 않는 동안 반복됩니다
    while stack:
        # 스택 가장 뒤의 값을 pop 합니다
        pop = stack.pop()
        # 만약 pop한 값이 끝 값이면 result를 1로 바꾸고 빠져나옵니다
        if pop == end:
            result = 1
            break

        # 끝이 아닐 경우 그래프(G)에서 pop한 노드의 index를 확인하고 연결된 노드를 확인합니다
        for new in G[pop]:
            # 방문한 적이 없으면 스택에 append하고
            if visit[new] == False:
                stack.append(new)
                # 스택에 넣으면서 방문 기록을 해줍니다
                visit[new] = True


    print(f"#{t + 1} {result}")

