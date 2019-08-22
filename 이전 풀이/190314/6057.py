import sys
sys.stdin = open("6057.txt")

for t in range(int(input())):
    # 노드 개수, 간선 개수
    node, line = map(int, input().split())
    # 각 노드가 어디를 가리키는지 표시하기 위한 리스트
    graph = [ [] for _ in range(node + 1) ]

    # 예시의 경우, 1이 2와 3을 가리키고 2는 3을 가리키기 때문에 다시 되돌아오는 과정이 없어서 양방향 그래프 리스트로 만들기
    for i in range(line):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    # 기준점이 되었던 노드를 확인하기 위한 리스트
    used = [True] * (node + 1)
    ans = 0
    for idx in range(1, node + 1):
        n, g_idx = 0, len(graph[idx])
        # 이 윗줄과 아랫줄을 합치면 for n in range(len(graph[idx]): 와 같음
        while n < g_idx:
            # 작업 순서
            # 기준점에 연결된 노드를 하나씩 보고 연결된 노드가 기준점 노드에 있는지 확인하는 식
            # 1) 1번 노드는 [2, 3]이고 1번 노드 안의 2번 노드는 [1, 3], 3번 노드는 [1, 2]
            # 2) 1번 노드의 첫 번째 연결 노드인 2번 노드 안에 있는 1과 3을 순서대로 봄
            # 3) 기준점이 된 적이 있는 노드는 패스, 기준점이 된 적이 없으면 다시 현재 기준점 노드와 연결되었는지 확인

            # 예시의 순서에선 1번 노드의 [2, 3] 중 [2]부터 보기 위한 변수, 이하 현재 노드
            new = graph[idx][n]
            chk = 0
            # 만약 현재 노드가 기준점이 된 적이 없다면 if문 진입
            # 체크하는 이유는 중복된 걸 건너뛰기 위해서
            if used[new]:
                # 현재 노드와 연결된 노드를 확인하기 위한 for문, 예시에선 2번 노드에 연결된 [1, 2] 중 1부터, 이하 탐색 노드
                for g_new in graph[new]:
                    # 탐색 노드가 기준점 노드와 연결된 노드고, 기준점이 된 적이 없으면 진입
                    if g_new in graph[idx] and used[g_new]:
                        # 먄악 진입했다면 기준점 노드 - 현재 노드 - 탐색 노드 - 기준점 노드로 연결되었기 때문에 삼각형이 성립
                        chk += 1
                # 만약 삼각형이 있다면 진입
                if chk:
                    # 기준점 노드와 연결되었던 것을 제거, 중복 제거를 위해서!
                    graph[idx].pop(n)
                    # 체크된 삼각형을 답에 더하기
                    ans += chk
                    # graph[idx].pop(n)을 했기 때문에 전체 length가 -1 감소했기 때문에 - 1
                    g_idx -= 1
                    continue

            # 만약 기준점이 된 적이 있는 노드라서 진입하지 못했거나, 삼각형이 된 적이 없다면 n이 + 1
            n += 1
        # 기준점이 되었던 것을 표시
        used[idx] = False

    print(f"#{t + 1} {ans}")