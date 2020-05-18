import sys
sys.stdin = open("15683.txt")


def go_cam(row, col, dir):

    for d in dir:
        if d == -1:
            d = 3
        if d == 4:
            d = 0

        if d == 0:
            r = row - 1
            while 0 <= r and office[r][col] != '6':
                if type(office[r][col]) == int:
                    office[r][col] += 1
                r -= 1
        elif d == 1:
            c = col + 1
            while c < width and office[row][c] != '6':
                if type(office[row][c]) == int:
                    office[row][c] += 1
                c += 1
        elif d == 2:
            r = row + 1
            while r < height and office[r][col] != '6':
                if type(office[r][col]) == int:
                    office[r][col] += 1
                r += 1
        elif d == 3:
            c = col - 1
            while 0 <= c and office[row][c] != '6':
                if type(office[row][c]) == int:
                    office[row][c] += 1
                c -= 1


def reset_cam(row, col, dir):

    for d in dir:
        if d == -1:
            d = 3
        if d == 4:
            d = 0

        if d == 0:
            r = row - 1
            while 0 <= r and office[r][col] != '6':
                if type(office[r][col]) == int:
                    office[r][col] -= 1
                r -= 1
        elif d == 1:
            c = col + 1
            while c < width and office[row][c] != '6':
                if type(office[row][c]) == int:
                    office[row][c] -= 1
                c += 1
        elif d == 2:
            r = row + 1
            while r < height and office[r][col] != '6':
                if type(office[r][col]) == int:
                    office[r][col] -= 1
                r += 1
        elif d == 3:
            c = col - 1
            while 0 <= c and office[row][c] != '6':
                if type(office[row][c]) == int:
                    office[row][c] -= 1
                c -= 1


def check_office():
    global answer
    point = 0

    for row in range(height):
        for col in range(width):
            if office[row][col] == 0:
                point += 1

    if answer > point:
        answer = point


def check_cam(idx):

    if idx == len(cam):
        check_office()
        return

    row, col = cam[idx]
    if office[row][col] == '1':
        for i in range(4):
            go_cam(row, col, [i])
            check_cam(idx + 1)
            reset_cam(row, col, [i])

    elif office[row][col] == '2':
        for i in range(2):
            go_cam(row, col, [i, i + 2])
            check_cam(idx + 1)
            reset_cam(row, col, [i, i + 2])

    elif office[row][col] == '3':
        for i in range(4):
            go_cam(row, col, [i, i + 1])
            check_cam(idx + 1)
            reset_cam(row, col, [i, i + 1])

    elif office[row][col] == '4':
        for i in range(4):
            go_cam(row, col, [i - 1, i, i + 1])
            check_cam(idx + 1)
            reset_cam(row, col, [i - 1, i, i + 1])

    elif office[row][col] == '5':
        go_cam(row, col, [0, 1, 2, 3])
        check_cam(idx + 1)
        reset_cam(row, col, [0, 1, 2, 3])


for T in range(int(input())):
    answer = 0xffffffff
    height, width = map(int, input().split())
    office = []
    cam = []
    for row in range(height):
        inputs = input().split()
        for col in range(width):
            if inputs[col] == '6':
                continue
            if inputs[col] == '0':
                inputs[col] = 0
            else:
                cam.append((row, col))
        office.append(inputs)

    check_cam(0)

    print(answer)

