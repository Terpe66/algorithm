import sys
sys.stdin = open("1211.txt")

for T in range(10):
    TC = input()
    ladder = [input().split() for _ in range(100)]
    # S : stack
    S = []
    # ans : 0번 index는 사다리의 출발 index, 1번 index는 사다리의 이동 거리입니다
    ans = (0, 0xffffff)
    for i in range(100):
        # 맨 첫 번째 줄에서 출발하기 때문에 ladder[0]으로 고정합니다
        if ladder[0][i] == "1":
            # 출발 지점(1)을 찾으면 스택에 집어넣고
            S.append((i, 0))
            # y : 아래로 내려가는 index를 정의해줍니다
            y = 1
            # 스택이 비어있지 않으면 계속 진행됩니다
            while S:
                # idx : 좌우를 탐색하는 index 변수, cnt : 이동 거리
                idx, cnt = S.pop()
                # y < 100 : 가장 아래로 내려갔을 때 반복문이 종료되게 하기 위한 조건
                while y < 100:
                    # 좌우 index 범위 지정을 꼭 해주고,
                    # 현재 상하 위치[y]의 왼쪽[idx - 1]이 "1"이면 진입합니다
                    if 0 <= idx - 1 < 100 and ladder[y][idx - 1] == "1":
                        # 현재 상하 위치[y]의 왼쪽[idx - 1]이 "1"일 동안 계속 왼쪽으로 진행합니다
                        while 0 <= idx - 1 < 100 and ladder[y][idx - 1] != "0":
                            # 왼쪽이 "1"이 아닐 때까지 idx를 1씩 감소시키고 이동 거리 cnt를 1씩 증가시킵니다
                            idx -= 1
                            cnt += 1
                        # while문이 종료(더 이상 왼쪽에 "1"이 없으면 내려가야 하기 때문에)되면 스택에 현재 idx와 cnt를 넣어줍니다
                        S.append((idx, cnt))
                        # 다시 오른쪽으로 이동하는 걸 막기 위해 바로 아래로 1칸 내려주기 위해 y를 1 증가시킵니다
                        y += 1
                        break
                    # 왼쪽 이동과 같은 동작을 오른쪽을 바라보면서 합니다
                    elif 0 <= idx + 1 < 100 and ladder[y][idx + 1] == "1":
                        while 0 <= idx + 1 < 100 and ladder[y][idx + 1] != "0":
                            idx += 1
                            cnt += 1
                        S.append((idx, cnt))
                        y += 1
                        break
                    # 좌우 모두 "1"이 아닐 경우 아래로 내려가면서 이동 거리를 1씩 증가시킵니다
                    y += 1
                    cnt += 1

            # 현재 정답의 이동 거리가 현재 탐색한 이동 거리보다 작을 경우 ans를 변경해줍니다
            if ans[1] > cnt:
                ans = (i, cnt)

    print(f"#{TC} {ans[0]}")