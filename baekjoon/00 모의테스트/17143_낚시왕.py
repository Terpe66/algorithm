import sys
sys.stdin = open("17143.txt")


def shark_move(row, col, next):

    speed, dir, size, cur = sea[row][col]
    r, c = row, col
    if dir == 1:
        if speed > row:
            r = (speed - row) % (height - 1)
            if ((speed - row) // (height - 1)) % 2 == 0:
                dir = 2
            else:
                r = height - 1 - r
        else:
            r = row - speed
        if r == 0:
            dir = 1
        if r == height - 1:
            dir = 2
    elif dir == 2:
        if (speed + row) > height - 1:
            r = ((speed + row) % (height - 1))
            if ((speed + row) // (height - 1)) % 2:
                dir = 1
                r = height - 1 - r
        else:
            r = row + speed
        if r == 0:
            dir = 1
        if r == height - 1:
            dir = 2
    elif dir == 3:
        if (speed + col) > width - 1:
            c = ((speed + col) % (width - 1))
            if ((speed + col) // (width - 1)) % 2:
                dir = 4
                c = width - 1 - c
        else:
            c = col + speed
        if c == 0:
            dir = 4
        if c == width - 1:
            dir = 3
    elif dir == 4:
        if speed > col:
            c = (speed - col) % (width - 1)
            if ((speed - col) // (width - 1)) % 2 == 0:
                dir = 3
            else:
                c = width - 1 - c
        else:
            c = col - speed
        if c == 0:
            dir = 4
        if c == width - 1:
            dir = 3

    temp = [speed, dir, size, next]
    sea[row][col] = []
    if not sea[r][c]:
        sea[r][c] = temp
        return
    if r == row and c == col:
        sea[r][c] = temp
        return
    if sea[r][c][3] != next:
        shark_move(r, c, next)
        if sea[r][c] and sea[r][c][2] < size:
            sea[r][c] = temp
            return
        if not sea[r][c]:
            sea[r][c] = temp
            return
    if sea[r][c][3] == next and sea[r][c][2] < size:
        sea[r][c] = temp
        return


for T in range(int(input())):
    height, width, shark = map(int, input().split())

    answer = 0
    if shark:
        sea = [[[] for _ in range(width)] for _ in range(height)]
        for _ in range(shark):
            r, c, s, d, z = map(int, input().split())
            sea[r - 1][c - 1] = [s, d, z, 0]

        cur = taegong = 0
        while taegong < width:
            next = (cur + 1) % 2
            for r in range(height):
                if sea[r][taegong]:
                    answer += sea[r][taegong][2]
                    sea[r][taegong] = []
                    break


            for row in range(height):
                for col in range(width):
                    if sea[row][col] and sea[row][col][3] == cur:
                        shark_move(row, col, next)

            cur = next
            taegong += 1

    print(answer)
