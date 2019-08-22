import sys
sys.stdin = open("5521.txt")

from collections import deque

for t in range(int(input())):
    # human : 전체 사람(노드)의 수, line : 간선 수
    human, line = map(int, input().split())
    # friends : 각 노드별로 이어진 노드를 넣기 위한 리스트
    friends = [[] for _ in range(human + 1)]

    # 간선의 수만큼 for문 반복
    for _ in range(line):
        # x : 간선의 시작점, y : 간선의 도착점
        x, y = map(int, input().split())
        # 문제 상 x -> y로 이어져 있더라도 x와 y가 친한 사이이기 때문에 양방향 노드로 진행해야 한다
        # 그래서 friends의 x번째 index에 y를, y번째 index에 x를 넣어서 서로 연결된 걸 확인한다
        friends[x].append(y)
        friends[y].append(x)

    # 한 번 도착한 노드(한 번 초대한 사람)에는 다시 방문하지 않기 위해 체크하는 리스트
    chk = [False] * (human + 1)
    # Q는 deque로 만들었지만 그냥 list로 만들고 pop(0)으로 뽑아도 된다(시간이 조금 느려짐)
    Q = deque()
    ans = 0
    # Q에 노드의 시작인 1번 index값과 0을 넣어준다.
    # 문제 상 1번의 친구, 그 친구의 친구까지만 초대하는 것이기 때문에 시작인 1번에서 몇 번째 친구인지 세는 count 값을 0으로 설정
    Q.append((1, 0))
    # 생일 당사자는 세지 않기 때문에 chk[1]을 True로 변경
    chk[1] = True

    # 진행은 BFS
    # Queue로 가장 앞의 index 값을 빼내면서 진행하는 게 BFS
    # Stack으로 가장 뒤의 index값을 빼면서 진행하는 게 DFS

    # Q에 값이 없을 때까지 진행
    while Q:
        # x : 친구가 있는지 확인할 현재 사람, cnt : 몇 번째 건넌 친구인지 확인하는 count 값
        x, cnt = Q.popleft()
        # x번 친구의 친구들을 모두 뽑아내야 하기 때문에 friends[x]의 값이 없을 때까지 while문 진행
        while friends[x]:
            # new : friends[x]에서 pop한 값(새로운 친구)
            new = friends[x].pop()
            # chk[new] == False : 새로 뽑은 노드(친구)가 다른 노드에서 뽑힌 노드인지 아닌지 확인,
            # cnt + 1 < 3 : cnt가 2보다 작으면 진행, cnt가 2 이상이면 친구의 친구의 친구까지 초대하는 게 되기 때문에 안 된다
            # cnt < 2로 해도 됩니다
            if chk[new] == False and cnt + 1 < 3:
                # Q에 새 친구와 cnt + 1을 넣어서 몇 번 건너 친구인지 확인할 수 있게 한다
                Q.append((new, cnt + 1))
                # 집어 넣은 친구를 집어 넣었다고 확인
                chk[new] = True
                # 초대된 친구의 숫자를 1 증가
                ans += 1

    print(f"#{t + 1} {ans}")