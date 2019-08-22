from collections import deque
import sys
sys.stdin = open("5015.txt")

for t in range(int(input())):
    size = int(input())

    maze = []
    for _ in range(size):
        maze.append([i for i in input()])

    row, goal_x, goal_y = 0, -1, -1
    S = deque([])
    while -1 == goal_x or S == deque([]):
        for col in range(size):
            if maze[row][col] == "3":
                goal_x, goal_y = row, col
            if maze[row][col] == "2":
                S.appendleft([row, col])
        row += 1

    start = row_col = S.popleft()
    row, col = row_col[0], row_col[1]
    C = deque([])
    cnt = 0
    while maze[row][col] != maze[goal_x][goal_y]:
        if row == 0:
            if col == 0:
                if "3" in (maze[row][col+1], maze[row+1][col]):
                    break
                if maze[row][col+1] == "0":
                    S.appendleft([row, col+1])
                    C.appendleft(cnt)
                if maze[row+1][col] == "0":
                    S.appendleft([row+1, col])
                    C.appendleft(cnt)
            elif col == size-1:
                if "3" in (maze[row+1][col], maze[row][col-1]):
                    break
                if maze[row+1][col] == "0":
                    S.appendleft([row+1, col])
                    C.appendleft(cnt)
                if maze[row][col-1] == "0":
                    S.appendleft([row, col-1])
                    C.appendleft(cnt)
            else:
                if "3" in (maze[row][col+1], maze[row+1][col], maze[row][col-1]):
                    break
                if maze[row][col+1] == "0":
                    S.appendleft([row, col+1])
                    C.appendleft(cnt)
                if maze[row+1][col] == "0":
                    S.appendleft([row+1, col])
                    C.appendleft(cnt)
                if maze[row][col-1] == "0":
                    S.appendleft([row, col-1])
                    C.appendleft(cnt)
        elif row == size-1:
            if col == 0:
                if "3" in (maze[row][col+1], maze[row-1][col]):
                    break
                if maze[row-1][col] == "0":
                    S.appendleft([row-1, col])
                    C.appendleft(cnt)
                if maze[row][col+1] == "0":
                    S.appendleft([row, col+1])
                    C.appendleft(cnt)
            elif col == size-1:
                if "3" in (maze[row-1][col], maze[row][col-1]):
                    break
                if maze[row-1][col] == "0":
                    S.appendleft([row-1, col])
                    C.appendleft(cnt)
                if maze[row][col-1] == "0":
                    S.appendleft([row, col-1])
                    C.appendleft(cnt)
            else:
                if "3" in (maze[row-1][col], maze[row][col+1], maze[row][col-1]):
                    break
                if maze[row-1][col] == "0":
                    S.appendleft([row-1, col])
                    C.appendleft(cnt)
                if maze[row][col+1] == "0":
                    S.appendleft([row, col+1])
                    C.appendleft(cnt)
                if maze[row][col-1] == "0":
                    S.appendleft([row, col-1])
                    C.appendleft(cnt)
        else:
            if col == 0:
                if "3" in (maze[row-1][col], maze[row][col+1], maze[row+1][col]):
                    break
                if maze[row-1][col] == "0":
                    S.appendleft([row-1, col])
                    C.appendleft(cnt)
                if maze[row][col+1] == "0":
                    S.appendleft([row, col+1])
                    C.appendleft(cnt)
                if maze[row+1][col] == "0":
                    S.appendleft([row+1, col])
                    C.appendleft(cnt)
            elif col == size-1:
                if "3" in (maze[row-1][col], maze[row+1][col], maze[row][col-1]):
                    break
                if maze[row-1][col] == "0":
                    S.appendleft([row-1, col])
                    C.appendleft(cnt)
                if maze[row+1][col] == "0":
                    S.appendleft([row+1, col])
                    C.appendleft(cnt)
                if maze[row][col-1] == "0":
                    S.appendleft([row, col-1])
                    C.appendleft(cnt)
            else:
                if "3" in (maze[row-1][col], maze[row][col+1], maze[row+1][col], maze[row][col-1]):
                    break
                if maze[row-1][col] == "0":
                    S.appendleft([row-1, col])
                    C.appendleft(cnt)
                if maze[row][col+1] == "0":
                    S.appendleft([row, col+1])
                    C.appendleft(cnt)
                if maze[row+1][col] == "0":
                    S.appendleft([row+1, col])
                    C.appendleft(cnt)
                if maze[row][col-1] == "0":
                    S.appendleft([row, col-1])
                    C.appendleft(cnt)

        if S == deque([]):
            cnt = 0
            break
        else:
            row_col = S.popleft()
            cnt = C.popleft()
            row, col = row_col[0], row_col[1]

        maze[row][col] = "1"
        cnt += 1

    print(f"#{t+1} {cnt}")