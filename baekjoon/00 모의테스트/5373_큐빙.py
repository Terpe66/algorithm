import sys
sys.stdin = open("5373.txt")


def turn_qube(side, clock):
    if clock == -1:
        a, b, c, d, e, f, g, h = 2, 8, 6, 0, 5, 7, 3, 1
    else:
        a, b, c, d, e, f, g, h = 6, 0, 2, 8, 3, 1, 5, 7

    qube[side][0], qube[side][2], qube[side][8], qube[side][6] = qube[side][a], qube[side][b], qube[side][c], qube[side][d]
    qube[side][1], qube[side][5], qube[side][7], qube[side][3] = qube[side][e], qube[side][f], qube[side][g], qube[side][h]

    side_turn(side, clock)


def side_turn(side, clock):
    if side == 0:
        if clock == -1:
            team_row = [1, 4, 3, 2]
            team_col = [[0, 1, 2], [8, 7, 6], [0, 1, 2], [0, 1, 2]]
        else:
            team_row = [1, 2, 3, 4]
            team_col = [[0, 1, 2], [0, 1, 2], [0, 1, 2], [8, 7, 6]]
    elif side == 5:
        if clock == -1:
            team_row = [1, 2, 3, 4]
            team_col = [[6, 7, 8], [6, 7, 8], [6, 7, 8], [2, 1, 0]]
        else:
            team_row = [1, 4, 3, 2]
            team_col = [[6, 7, 8], [2, 1, 0], [6, 7, 8], [6, 7, 8]]
    elif side == 1:
        team_col = [[0, 3, 6], [0, 3, 6], [0, 3, 6], [0, 3, 6]]
        if clock == -1:
            team_row = [0, 2, 5, 4]
        else:
            team_row = [0, 4, 5, 2]
    elif side == 3:
        team_col = [[2, 5, 8], [2, 5, 8], [2, 5, 8], [2, 5, 8]]
        if clock == -1:
            team_row = [0, 4, 5, 2]
        else:
            team_row = [0, 2, 5, 4]
    elif side == 2:
        if clock == -1:
            team_row = [0, 3, 5, 1]
            team_col = [[6, 7, 8], [0, 3, 6], [2, 1, 0], [8, 5, 2]]
        else:
            team_row = [0, 1, 5, 3]
            team_col = [[6, 7, 8], [8, 5, 2], [2, 1, 0], [0, 3, 6]]
    elif side == 4:
        if clock == -1:
            team_row = [0, 1, 5, 3]
            team_col = [[0, 1, 2], [6, 3, 0], [8, 7, 6], [2, 5, 8]]
        else:
            team_row = [0, 3, 5, 1]
            team_col = [[0, 1, 2], [2, 5, 8], [8, 7, 6], [6, 3, 0]]

    temp = []
    for i in range(3):
        temp.append(qube[team_row[0]][team_col[0][i]])

    for i in range(3):
        for c in range(3):
            qube[team_row[i]][team_col[i][c]] = qube[team_row[i + 1]][team_col[i + 1][c]]

    for c in range(3):
        qube[team_row[-1]][team_col[-1][c]] = temp[c]


for T in range(int(input())):
    qube = [['w'] * 9, ['g'] * 9, ['r'] * 9, ['b'] * 9, ['o'] * 9, ['y'] * 9]
    N = int(input())
    turns = input().split()
    for turn in turns:
        if turn[0] == 'U':
            side = 0
        elif turn[0] == 'L':
            side = 1
        elif turn[0] == 'F':
            side = 2
        elif turn[0] == 'R':
            side = 3
        elif turn[0] == 'B':
            side = 4
        elif turn[0] == 'D':
            side = 5
        if turn[1] == '+':
            clock = 0
        else:
            clock = -1
        turn_qube(side, clock)

    start, end = 0, 3
    print(T + 1)
    for _ in range(3):
        for i in range(start, end):
            print(qube[0][i], end="")
        print()
        start += 3
        end += 3