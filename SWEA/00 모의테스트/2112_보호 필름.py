import sys
sys.stdin = open("2112.txt")


def reset(r):
    for c in range(width):
        good[r][c] = screen[r][c]


def make_good(idx, deep, cnt, n):
    global answer

    if n > -1:
        for c in range(width):
            good[idx - 1][c] = n

    if deep == cnt:
        if check_screen():
            answer = min(answer, cnt)
            return True
        return False

    for i in range(idx, height):
        if make_good(i + 1, deep + 1, cnt, 0):
            reset(i)
            return True
        if make_good(i + 1, deep + 1, cnt, 1):
            reset(i)
            return True
        reset(i)


def check_screen():
    for col in range(width):
        cnt = 1
        before = good[0][col]
        for row in range(1, height):
            if good[row][col] == before:
                cnt += 1
            else:
                before = good[row][col]
                cnt = 1

            if cnt == K:
                break
        else:
            return False
    return True


for T in range(int(input())):
    height, width, K = map(int, input().split())
    screen = [list(map(int, input().split())) for _ in range(height)]
    good = [[0] * width for _ in range(height)]

    for r in range(height):
        for c in range(width):
            good[r][c] = screen[r][c]

    answer = height
    for i in range(K + 1):
        if make_good(0, 0, i, -1):
            break

    print("#{} {}".format(T + 1, answer))
