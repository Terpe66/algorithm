import sys
sys.stdin = open("5656.txt")


def reblock():
    for col in range(width):
        for row in range(height - 1, -1, -1):
            if copy_board[row][col] == 0:
                r = row
                while 0 <= r:
                    if copy_board[r][col] == 0:
                        break
                    r -= 1

                nr = r - 1
                while 0 <= nr:
                    if copy_board[nr][col] != 0:
                        break
                    nr -= 1

                if nr == -1:
                    break
                copy_board[r][col], copy_board[nr][col] = copy_board[nr][col], 0


def break_block(selected):

    count = block_cnt
    for col in selected:
        for row in range(height):
            if copy_board[row][col] > 0:
                temp = [(row, col, copy_board[row][col])]
                copy_board[row][col] = 0
                count -= 1
                while temp:
                    r, c, cnt = temp.pop()
                    for nr in range(r - cnt + 1, r + cnt):
                        if nr < 0:
                            continue
                        if nr >= height:
                            break

                        if copy_board[nr][c] > 1:
                            temp.append((nr, c, copy_board[nr][c]))
                            copy_board[nr][c] = 0
                            count -= 1
                        elif copy_board[nr][c] == 1:
                            copy_board[nr][c] = 0
                            count -= 1

                    for nc in range(c - cnt + 1, c + cnt):
                        if nc < 0:
                            continue
                        if nc >= width:
                            break

                        if copy_board[r][nc] > 1:
                            temp.append((r, nc, copy_board[r][nc]))
                            copy_board[r][nc] = 0
                            count -= 1
                        elif copy_board[r][nc] == 1:
                            copy_board[r][nc] = 0
                            count -= 1

                reblock()
                break

    return count


def select_block(deep, shot, selected):
    global answer

    if deep == shot:
        now = break_block(selected)
        answer = min(answer, now)
        copy()
        return

    for i in range(width):
        select_block(deep + 1, shot, selected + [i])


def copy():
    for row in range(height):
        for col in range(width):
            copy_board[row][col] = board[row][col]


for T in range(int(input())):
    answer = 0xffffffff
    shot, width, height = map(int, input().split())
    board = [[0] * width for _ in range(height)]
    copy_board = [[0] * width for _ in range(height)]
    block_cnt = 0

    for row in range(height):
        inputs = list(map(int, input().split()))
        for col in range(width):
            board[row][col] = inputs[col]
            copy_board[row][col] = inputs[col]
            if inputs[col] > 0:
                block_cnt += 1

    select_block(0, shot, [])

    print("#{} {}".format(T + 1, answer))
