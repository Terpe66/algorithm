import sys
sys.stdin = open("2382.txt")

class Bug:
    def __init__(self, row, col, bugs, dir, name, cnt):
        self.row = row
        self.col = col
        self.bugs = bugs
        self.dir = dir
        self.name = name
        self.cnt = cnt

for T in range(int(input())):
    size, time, bug = map(int, input().split())
    Map = [[[] for j in range(size)] for i in range(size)]
    bugs = [0] * bug
    for i in range(bug):
        row, col, bs, dir = map(int, input().split())
        bugs[i] = Bug(row, col, bs, dir, i, 0)
        Map[bugs[i].row][bugs[i].col].append(bugs[i])

    t = 0
    while t < time:
        for i in range(bug):
            if bugs[i]:
                if len(Map[bugs[i].row][bugs[i].col]) > 1:
                    max_bugs = sum_bugs = tmp_dir = 0
                    tmp_name = []
                    for j in range(len(Map[bugs[i].row][bugs[i].col])):
                        if Map[bugs[i].row][bugs[i].col][j].cnt == t:
                            tmp_name.append(Map[bugs[i].row][bugs[i].col][j].name)
                            sum_bugs += Map[bugs[i].row][bugs[i].col][j].bugs
                            if Map[bugs[i].row][bugs[i].col][j].bugs > max_bugs:
                                max_bugs = Map[bugs[i].row][bugs[i].col][j].bugs
                                tmp_dir = Map[bugs[i].row][bugs[i].col][j].dir
                    if tmp_name:
                        bugs[i].bugs, bugs[i].dir = sum_bugs, tmp_dir
                        for j in range(bug):
                            if bugs[j] and bugs[j].name in tmp_name and bugs[j].name != bugs[i].name:
                                Map[bugs[j].row][bugs[j].col].remove(bugs[j])
                                bugs[j] = False
                Map[bugs[i].row][bugs[i].col].remove(bugs[i])

                if bugs[i].dir == 1:
                    bugs[i].row -= 1
                elif bugs[i].dir == 2:
                    bugs[i].row += 1
                elif bugs[i].dir == 3:
                    bugs[i].col -= 1
                elif bugs[i].dir == 4:
                    bugs[i].col += 1

                if bugs[i].row == 0 or bugs[i].row == size - 1 or bugs[i].col == 0 or bugs[i].col == size - 1:
                    bugs[i].bugs //= 2
                    if bugs[i].dir % 2:
                        bugs[i].dir += 1
                    else:
                        bugs[i].dir -= 1

                # print((bugs[i].row, bugs[i].col, bugs[i].name, bugs[i].dir), size)
                Map[bugs[i].row][bugs[i].col].append(bugs[i])
                bugs[i].cnt += 1
        t += 1

    sum_bugs = 0
    for i in range(bug):
        if bugs[i]:
            sum_bugs += bugs[i].bugs

    print(f"#{T + 1} {sum_bugs}")