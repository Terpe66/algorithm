import sys, copy
sys.stdin = open("5656.txt")

def find(n=0, idx=0):
    if n == N:
        for i in range(N):
            shot(0, order[i])
            reset_board(order[i])
        reset_set()
        return

    for i in range(width):
        order[idx] = i
        find(n + 1, idx + 1)


def shot(row=0, col=0):
    global reset

    while row < height:
        if board[row][col] == 0:
            pass
        elif board[row][col] == 1:
            reset.add((row, col, board[row][col]))
            board[row][col] = 0
        else:
            i = board[row][col] - 1
            reset.add((row, col, board[row][col]))
            board[row][col] = 0
            min_col, max_col = col - i, col + i
            min_row, max_row = row - i, row + i
            while min_col <= max_col:
                if 0 <= min_col < width:
                    if board[row][min_col] != 0:
                        reset.add((row, min_col, board[row][min_col]))
                        shot(row, min_col)
                min_col += 1

            while min_row <= max_row:
                if 0 <= min_row < height:
                    if board[min_row][col] != 0:
                        reset.add((min_row, col, board[min_row][col]))
                        if board[min_row][col] == 1:
                            board[min_row][col] = 0
                        else:
                            shot(min_row, col)
                min_row += 1
        row += 1


def reset_board(col):
    global board

    search_row = height - 1

    while 0 <= search_row:
        if board[search_row][col] == 0:
            now_row = search_row
            while 0 <= now_row:
                if board[now_row][col] != 0:
                    board[search_row][col], board[now_row][col] = board[now_row][col], board[search_row][col]
                now_row -= 1
        search_row -= 1


def reset_set():
    global reset, ans, real_ans, board

    if ans - len(reset) < real_ans:
        real_ans = ans - len(reset)

    board = copy.deepcopy(Board)

    reset = set()

for t in range(int(input())):
    N, width, height = map(int, input().split())
    real_ans = 0
    Board = []
    for i in range(height):
        inputs = list(map(int, input().split()))
        real_ans += width - inputs.count(0)
        Board.append(inputs)
    board = copy.deepcopy(Board)

    ans = real_ans
    reset = set()

    order = [N + 1] * N
    find()

    print(real_ans)
    break

