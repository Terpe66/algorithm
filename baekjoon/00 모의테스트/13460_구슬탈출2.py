import sys
sys.stdin = open("13460.txt")


def balling(dir, count, red, blue):
    global answer

    if count >= answer or count > 10:
        return

    for i in range(4):
        if i == dir:
            continue
        first, second = blue, red
        if i == 0 and red[0] < blue[0]:
            first, second = red, blue
        elif i == 1 and red[1] > blue[1]:
            first, second = red, blue
        elif i == 2 and red[0] > blue[0]:
            first, second = red, blue
        elif i == 3 and red[1] < blue[1]:
            first, second = red, blue

        red_check = blue_check = False
        for now in [first, second]:
            nr, nc = now
            while True:
                nr, nc = nr + drc[i][0], nc + drc[i][1]
                if board[nr][nc] == "O":
                    if now == red:
                        red_check = True
                    else:
                        blue_check = True
                    break
                if board[nr][nc] == "#":
                    nr, nc = nr - drc[i][0], nc - drc[i][1]
                    break

            if blue_check:
                continue

            if now == red:
                left = (nr, nc)
            else:
                right = (nr, nc)

        if red_check:
            answer = count
            return

        if left == right:
            if second == red:
                left = (left[0] - drc[i][0], left[1] - drc[i][1])
            else:
                right = (right[0] - drc[i][0], right[1] - drc[i][1])

        balling(i, count + 1, left, right)


drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for T in range(int(input())):
    answer = 0xffffffff
    height, width = map(int, input().split())
    board = [list(input()) for _ in range(height)]
    ball = [(), ()]

    for row in range(height):
        for col in range(width):
            if board[row][col] == "B":
                ball[1] = (row, col)
            elif board[row][col] == "R":
                ball[0] = (row, col)

    balling(-1, 1, ball[0], ball[1])
    if answer == 0xffffffff:
        answer = -1

    print("#{} {}".format(T + 1, answer))

import sys

sys.stdin = open("13460.txt")


def balling(dir, count, red, blue):
    global answer

    if count >= answer or count > 10:
        return 0xFFFFFFFF

    for i in range(4):
        if i == dir:
            continue

        is_red_first = False
        rRow, rCol = red
        bRow, bCol = blue
        if i == 0 and rRow < bRow:
            is_red_first = True
        elif i == 1 and rCol > bCol:
            is_red_first = True
        elif i == 2 and rRow > bRow:
            is_red_first = True
        elif i == 3 and rCol < bCol:
            is_red_first = True

        bRow, bCol = blue
        while True:
            bRow, bCol = bRow + drc[i][0], bCol + drc[i][1]
            if board[bRow][bCol] == "O":
                return 0xFFFFFFFF
            if board[bRow][bCol] == "#":
                bRow, bCol = bRow - drc[i][0], bCol - drc[i][1]
                break
        next_blue = (bRow, bCol)

        rRow, rCol = red
        while True:
            rRow, rCol = rRow + drc[i][0], rCol + drc[i][1]
            if board[rRow][rCol] == "O":
                return count
            if board[rRow][rCol] == "#":
                rRow, rCol = rRow - drc[i][0], rCol - drc[i][1]
                break
        next_red = (rRow, rCol)

        if next_red == next_blue:
            if is_red_first:
                next_blue = (next_blue[0] - drc[i][0], next_blue[1] - drc[i][1])
            else:
                next_red = (next_red[0] - drc[i][0], next_red[1] - drc[i][1])

        ret = balling(i, count + 1, next_red, next_blue)
        if answer > ret:
            answer = ret

    return answer


drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for T in range(int(input())):
    answer = 0xffffffff
    height, width = map(int, input().split())
    board = [list(input()) for _ in range(height)]
    ball = [(), ()]

    for row in range(height):
        for col in range(width):
            if board[row][col] == "B":
                ball[1] = (row, col)
            elif board[row][col] == "R":
                ball[0] = (row, col)

    answer = balling(-1, 1, ball[0], ball[1])
    if answer == 0xffffffff:
        answer = -1

    print("#{} {}".format(T + 1, answer))
