import sys
sys.stdin = open("5656.txt")

from collections import deque

def block(count, new):
    global ans

    if count == 0:
        if ans > new:
            ans = new
        return

    for col in range(width):
        for row in range(height):
            if board[row][col] != "0" and visited[row][col] == False:
                block_list.append((row, col, board[row][col]))

                for i in range(4):
                    chk = int(board[row][col])
                    if i == 0:
                        nr = row
                        while 0 <= nr and chk:
                            if visited[nr][col] == False:
                                if board[nr][col] != "0":
                                    block_list.append((nr, col, board[nr][col], count - 1))
                                    backup.append((nr, c))
                                    visited[nr][c] = True

                                chk -= 1
                            nr -= 1

                    elif i == 1:
                        nr = r
                        while nr < height and chk:
                            if visited[nr][c] == False:
                                if board[nr][c] != "0":
                                    Q.append((nr, c, board[nr][c], count - 1))
                                    backup.append((nr, c))
                                    visited[nr][c] = True
                                chk -= 1
                            nr += 1

                    elif i == 2:
                        nc = c
                        while 0 <= nc and chk:
                            if visited[r][nc] == False:
                                if board[r][nc] != "0":
                                    Q.append((r, nc, board[r][nc], count - 1))
                                    backup.append((r, nc))
                                    visited[r][nc] = True
                                chk -= 1
                            nc -= 1

                    elif i == 3:
                        nc = c
                        while nc < width and chk:
                            if visited[r][nc] == False:
                                if board[r][nc] != "0":
                                    Q.append((r, nc, board[r][nc], count - 1))
                                    backup.append((r, nc))
                                    visited[r][nc] = True
                                chk -= 1
                            nc += 1


for t in range(int(input())):
    count, width, height = map(int, input().split())

    board = [input().split() for _ in range(height)]
    visited = [[False] * width for _ in range(height)]
    block_list = deque()
    backup = []


    print(Q)