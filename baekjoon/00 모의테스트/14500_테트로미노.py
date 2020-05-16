import sys
sys.stdin = open("14500.txt")


def square(row, col):
    point = 0
    if 0 <= row - 1 and 0 <= col - 1:
        new = board[row - 1][col - 1] + board[row - 1][col] + board[row][col - 1] + board[row][col]
        if point < new:
            point = new

    return point


def zig(row, col):
    point = 0
    if 0 <= row - 1 and 0 <= col - 2:
        new = board[row - 1][col - 2] + board[row - 1][col - 1] + board[row][col - 1] + board[row][col]
        if point < new:
            point = new

    if row + 1 < height and 0 <= col - 2:
        new = board[row + 1][col - 2] + board[row + 1][col - 1] + board[row][col - 1] + board[row][col]
        if point < new:
            point = new

    if 0 <= row - 2 and 0 <= col - 1:
        new = board[row - 2][col - 1] + board[row - 1][col - 1] + board[row - 1][col] + board[row][col]
        if point < new:
            point = new

    if 0 <= row - 2 and col + 1 < width:
        new = board[row - 2][col + 1] + board[row - 1][col + 1] + board[row - 1][col] + board[row][col]
        if point < new:
            point = new

    return point


def L(row, col):
    point = 0
    if 0 <= row - 2 and 0 <= col - 1:
        new = board[row - 2][col - 1] + board[row - 1][col - 1] + board[row][col - 1] + board[row][col]
        if point < new:
            point = new

    if 0 <= row - 1 and col + 2 < width:
        new = board[row - 1][col + 2] + board[row - 1][col + 1] + board[row - 1][col] + board[row][col]
        if point < new:
            point = new

    if row + 2 < height and col + 1 < width:
        new = board[row + 2][col + 1] + board[row + 1][col + 1] + board[row][col + 1] + board[row][col]
        if point < new:
            point = new

    if row + 1 < height and 0 <= col - 2:
        new = board[row + 1][col - 2] + board[row + 1][col - 1] + board[row + 1][col] + board[row][col]
        if point < new:
            point = new

    if 0 <= row - 1 and 0 <= col - 2:
        new = board[row - 1][col - 2] + board[row - 1][col - 1] + board[row - 1][col] + board[row][col]
        if point < new:
            point = new

    if 0 <= row - 2 and col + 1 < width:
        new = board[row - 2][col + 1] + board[row - 1][col + 1] + board[row][col + 1] + board[row][col]
        if point < new:
            point = new

    if row + 1 < height and col + 2 < width:
        new = board[row + 1][col + 2] + board[row + 1][col + 1] + board[row + 1][col] + board[row][col]
        if point < new:
            point = new

    if row + 2 < height and 0 <= col - 1:
        new = board[row + 2][col - 1] + board[row + 1][col - 1] + board[row][col - 1] + board[row][col]
        if point < new:
            point = new

    return point


def long(row, col):
    point = 0
    if 0 <= row - 3:
        new = board[row - 3][col] + board[row - 2][col] + board[row - 1][col] + board[row][col]
        if point < new:
            point = new

    if 0 <= col - 3:
        new = board[row][col - 3] + board[row][col - 2] + board[row][col - 1] + board[row][col]
        if point < new:
            point = new

    return point


def top(row, col):
    point = 0
    if 0 <= row - 1 and 0 <= col - 2:
        new = board[row - 1][col - 1] + board[row][col - 2] + board[row][col - 1] + board[row][col]
        if point < new:
            point = new

    if row + 1 < height and 0 <= col - 2:
        new = board[row][col - 2] + board[row][col - 1] + board[row][col] + board[row + 1][col - 1]
        if point < new:
            point = new

    if 0 <= row - 2 and 0 <= col - 1:
        new = board[row - 2][col] + board[row - 1][col - 1] + board[row - 1][col] + board[row][col]
        if point < new:
            point = new

    if 0 <= row - 2 and col + 1 < width:
        new = board[row - 2][col] + board[row - 1][col] + board[row - 1][col + 1] + board[row][col]
        if point < new:
            point = new

    return point



for T in range(int(input())):
    answer = 0
    height, width = map(int, input().split())
    board = []
    for _ in range(height):
        board.append(list(map(int, input().split())))

    squares = []
    zigs = []
    Ls = []
    longs = []
    tops = []

    for r in range(height):
        for c in range(width):
            p = max([square(r, c), zig(r, c), L(r, c), long(r, c), top(r, c)])
            if answer < p:
                answer = p

    print(answer)