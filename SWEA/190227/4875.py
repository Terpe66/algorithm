import sys
sys.stdin = open("4875.txt")


for t in range(int(input())):
    side = int(input())
    maze = []
    maze.append(["X"]*(side+2))
    for _ in range(side):
        maze.append(["X"] + " ".join(input()).split() + ["X"])
    maze.append(["X"]*(side+2))
    S = []
    row = 1
    while not S:
        for col in range(1, side+1):
            if maze[row][col] == "2":
                e_row, e_col = row, col
                S.append([e_row, e_col])
                break
        row += 1
    go = ("0", "3")
    M = []
    cnt = 0
    while maze[e_row][e_col] != "3":
        if not M and cnt == 1:
            break
        if not M:
            cnt = 1
            if maze[e_row-1][e_col] in go:
                M.append("u")
                S.append([e_row, e_col])
            if maze[e_row][e_col+1] in go:
                M.append("r")
                S.append([e_row, e_col])
            if maze[e_row+1][e_col] in go:
                M.append("d")
                S.append([e_row, e_col])
            if maze[e_row][e_col-1] in go:
                M.append("l")
                S.append([e_row, e_col])
        if M:
            dir = M.pop()
            e_row, e_col = S[-1][0], S[-1][1]
            S.pop()
            if dir == "u":
                while maze[e_row-1][e_col] in go:
                    e_row -= 1
                    if maze[e_row][e_col+1] in go:
                        M.append("r")
                        S.append([e_row, e_col])
                    if maze[e_row][e_col-1] in go:
                        M.append("l")
                        S.append([e_row, e_col])
            elif dir == "r":
                while maze[e_row][e_col+1] in go:
                    e_col += 1
                    if maze[e_row-1][e_col] in go:
                        M.append("u")
                        S.append([e_row, e_col])
                    if maze[e_row+1][e_col] in go:
                        M.append("d")
                        S.append([e_row, e_col])
            elif dir == "d":
                while maze[e_row+1][e_col] in go:
                    e_row += 1
                    if maze[e_row][e_col+1] in go:
                        M.append("r")
                        S.append([e_row, e_col])
                    if maze[e_row][e_col-1] in go:
                        M.append("l")
                        S.append([e_row, e_col])
            elif dir == "l":
                while maze[e_row][e_col-1] in go:
                    e_col -= 1
                    if maze[e_row-1][e_col] in go:
                        M.append("u")
                        S.append([e_row, e_col])
                    if maze[e_row+1][e_col] in go:
                        M.append("d")
                        S.append([e_row, e_col])

    if maze[e_row][e_col] == "3":
        print(f"#{t+1} 1")
    else:
        print(f"#{t+1} 0")