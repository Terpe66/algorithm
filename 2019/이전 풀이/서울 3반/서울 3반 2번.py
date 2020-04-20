import sys
sys.stdin = open("02.txt")


def find(row, col):
    global height, size
    if MAP[row][col] > height:
        height = MAP[row][col]
    island[row][col] = True

    if col + 1 < size and MAP[row][col+1] != 0 and not island[row][col+1]:
        find(row, col+1)

    if row + 1 < size and MAP[row+1][col] != 0 and not island[row+1][col]:
        find(row+1, col)


for t in range(int(input())):
    size = int(input())

    MAP = []
    for _ in range(size):
        MAP.append(list(map(int, input().split())))

    island = [[False]*size for _ in range(size)]

    cnt, height = 0, 0
    # for row in range(size):
    #     for col in range(size):
    #         if MAP[row][col] == 0 or island[row][col]:
    #             continue
    #
    #         find(row, col)
    #         cnt += 1


    for row in range(size):
        for col in range(size):
            if MAP[row][col] == 0:
                continue

            if MAP[row][col] > height:
                height = MAP[row][col]

            island[row][col] = True
            cnt += 1
            if row > 0:
                if col == 0:
                    if island[row-1][col]:
                        cnt -= 1
                else:
                    if island[row - 1][col] or island[row][col-1]:
                        cnt -= 1
            else:
                if col > 0:
                    if island[row][col-1]:
                        cnt -= 1

    print("#{} {} {}".format(t+1, cnt, height))
