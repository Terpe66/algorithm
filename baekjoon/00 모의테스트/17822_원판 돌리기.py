import sys
sys.stdin = open("17822.txt")


def sum_circles():
    point = 0
    for row in range(circle):
        point += sum(circles[next][row])

    return point


def return_check():
    for i in range(circle):
        check_circle[i] = False


def average_check():
    average_num = sum_circles()
    if average_num:
        i = 0
        for row in range(circle):
            for col in range(nums):
                if circles[next][row][col] > 0:
                    i += 1

        if i < 1:
            return

        average_num /= i
        for row in range(circle):
            for col in range(nums):
                if 0 < circles[next][row][col] < average_num:
                    circles[next][row][col] += 1
                elif 0 < circles[next][row][col] > average_num:
                    circles[next][row][col] -= 1


def delete_nums(row, col, num):

    check = False
    if num == circles[cur][row][col - 1]:
        check = True
        check_circle[row] = True
        circles[next][row][col] = 0

    if col == nums - 1:
        if num == circles[cur][row][0]:
            check = True
            check_circle[row] = True
            circles[next][row][col] = 0
    else:
        if num == circles[cur][row][col + 1]:
            check = True
            check_circle[row] = True
            circles[next][row][col] = 0

    if row < circle - 1:
        if num == circles[cur][row + 1][col]:
            check = True
            check_circle[row] = True
            circles[next][row][col] = 0

    if 0 < row:
        if num == circles[cur][row - 1][col]:
            check = True
            check_circle[row] = True
            circles[next][row][col] = 0

    if not check:
        circles[next][row][col] = circles[cur][row][col]


def turn_circle(clock, t):

    if clock == 0:
        for idx in idx_list:
            temp = [0] * nums
            for j in range(nums):
                temp[(j + t) % nums] = circles[cur][idx][j]
            circles[cur][idx] = temp
    else:
        for idx in idx_list:
            temp = [0] * nums
            for j in range(nums):
                temp[(j - t) % nums] = circles[cur][idx][j]
            circles[cur][idx] = temp

    for row in range(circle):
        for col in range(nums):
            if circles[cur][row][col] > 0:
                delete_nums(row, col, circles[cur][row][col])
            else:
                circles[next][row][col] = 0

    if True in check_circle:
        return_check()
    else:
        average_check()


for T in range(int(input())):
    circle, nums, turn = map(int, input().split())
    circles = [[list(map(int, input().split())) for _ in range(circle)], [[0] * nums for _ in range(circle)]]
    check_circle = [False] * circle

    cur = 0
    for _ in range(turn):
        next = (cur + 1) % 2
        idx, clock, t = map(int, input().split())
        idx_list = []
        for i in range(idx - 1, circle, idx):
            idx_list.append(i)

        turn_circle(clock, t)
        cur = next

    answer = sum_circles()
    print(answer)