from collections import deque
import sys
sys.stdin = open("3190.txt")

for T in range(int(input())):
    answer = 0
    length = int(input())
    apple = int(input())
    board = [[0] * (length + 1) for _ in range(length + 1)]
    snake = deque()
    snake.append([1, 1])

    for a in range(apple):
        row, col = map(int, input().split())
        board[row][col] = 1

    inputMove = {}
    for s in range(int(input())):
        t, dir = map(str, input().split())
        inputMove[int(t)] = dir

    d = 0
    time = 0
    while True:
        time += 1

        row, col = snake[0]
        if d == 0:
            col += 1
        elif d == 1:
            row += 1
        elif d == 2:
            col -= 1
        elif d == 3:
            row -= 1

        if 0 == row or length + 1 == row or 0 == col or length + 1 == col or [row, col] in snake:
            break

        snake.appendleft([row, col])
        if board[row][col] == 1:
            board[row][col] -= 1
        else:
            snake.pop()

        dir = inputMove.get(time, False)
        if dir == 'D':
            d += 1
            if d == 4:
                d = 0
        elif dir == 'L':
            d -= 1
            if d == -1:
                d = 3

    print(time)