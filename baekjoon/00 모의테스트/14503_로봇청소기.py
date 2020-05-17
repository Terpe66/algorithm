import sys
sys.stdin = open("14503.txt")


def clear(r, c, d):

    board[r][c] = '3'

    i = dIdx[d]
    nd = d
    visit = [False] * 4
    chk = False
    clearChk = True
    while False in visit:
        if not clearChk:
            break

        nr, nc = r + search[i], c + search[3 - i]
        visit[i] = True
        nd -= 1
        if nd == -1:
            nd = 3
        if 0 < nr < height - 1 and 0 < nc < width - 1 and board[nr][nc] == '0':
            chk = True
            clearChk = clear(nr, nc, nd)

        i = dIdx[nd]

    if not chk:
        if nd == 0:
            nr, nc = r + 1, c
        elif nd == 1:
            nr, nc = r, c - 1
        elif nd == 2:
            nr, nc = r - 1, c
        elif nd == 3:
            nr, nc = r, c + 1

        if 0 < nr < height - 1 and 0 < nc < width - 1 and board[nr][nc] != '1':
            clear(nr, nc, nd)
        return False


search = [0, 0, 1, -1]
dIdx = [0, 3, 1, 2]

for T in range(int(input())):
    answer = 0

    height, width = map(int, input().split())
    row, col, dir = map(int, input().split())
    board = [input().split() for _ in range(height)]

    clear(row, col, dir)

    for r in range(1, height - 1):
        for c in range(1, width - 1):
            if board[r][c] == '3':
                answer += 1

    print(answer)