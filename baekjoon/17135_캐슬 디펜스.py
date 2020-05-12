import sys
sys.stdin = open("17135.txt")


# def reset():
#
#     for row, col in enemy_position:
#         Map[row][col] = "1"
#
#
# def bow(cnt):
#
#     if cnt == 0:
#         for i in range(width):
#             if Map[height][i] == "S":
#                 bow_position.append((height, i))
#         return
#
#     for i in range(width):
#         if Map[height][i] == "0":
#             Map[height][i] = "S"
#             bow(cnt - 1)
#             Map[height][i] = "0"
#
#
# def kill():
#
#     for i in range(3):
#         row, col = bow_position[i]
#         r, c = row, col
#
#         R = 0
#         while height - R > 0:
#
#             for ran in range(1, rng + 1):
#                 nr, nc = r, c - ran
#                 mr, mc = r - ran, c + ran
#
#                 while nr >= r:
#                     if 0 <= nr < height and 0 <= nc < width: # and
#                         pass
#
#
# height, width, rng = map(int, input().split())
# Map = []
# enemy_position = []
# bow_position = []
# for _ in range(height):
#     inputs = input().split()
#     for i in range(width):
#         if inputs[i] == "1":
#             enemy_position.append((_, i))
#     Map.append(inputs)
#
# Map.append(["0"] * width)


import copy


def shoot(pos, d, c_enemy):
    global cnt
    for d in range(1, d + 1):
        for i in range(1, d + 1):
            print("f,i", N - i, pos - d + i)
            if 0 <= N - i < N and 0 <= pos - d + i < M and c_enemy[N - i][pos - d + i] == 1:
                cnt += 1
                c_enemy[N - i][pos - d + i] = 0
                return

        for j in range(1, d + 1):
             print("f,j", N - d - 1 + j, pos + j - 1)
             if 0 <= N - d - 1 + j < N and 0 <= pos + j - 1 < M and c_enemy[N - d - 1 + j][pos + j - 1] == 1:
                cnt += 1
                c_enemy[N - d - 1 + j][pos + j - 1] = 0
                return



def comb(depth, no_archer, no_castle):
    global cnt, max_cnt
    if no_archer > archer or no_castle > castle:
        return

    if depth == M:
        c_enemy = copy.deepcopy(enemy)
        # print(c_enemy[N - 1])
        # print(visit)
        # 이 위치에 오면 궁수가 배치 완료됨 visit안에 1로 포지션 fix
        cnt = 0
        for round in range(N):
            # for a in range(N):
            #     print(c_enemy[a])
            # print(visit)
            for i in range(M):
                if visit[i] == 1:
                    shoot(i, D, c_enemy)


            # 한 라운드가 끝나서 맵이 업데이트 되는 지점
            c_enemy.pop()
            c_enemy.insert(0, [0] * M)

            # print(cnt)
            if cnt > max_cnt:
                max_cnt = cnt
        return

    #archer
    visit[depth] = 1
    comb(depth + 1, no_archer + 1, no_castle)
    visit[depth] = 0

    #castle
    visit[depth] = 2
    comb(depth + 1, no_archer, no_castle + 1)
    visit[depth] = 0


for t in range(int(input())):
    N, M, D = map(int, input().split())
    enemy = [[] for _ in range(N)]
    for i in range(N):
        enemy[i] = list(map(int, input().split()))
    cnt = 0

    castle = M - 3
    archer = 3
    visit = [0] * M
    max_cnt = 0


    comb(0, 0, 0)
    # print(t + 1, max_cnt)

