import sys
sys.stdin = open("1249.txt")

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for tc in range(int(input())):
    length = int(input())
    route = [list(map(int, input())) for _ in range(length)]
    ans_list = [[0xffff] * (length) for _ in range(length)]
    ans = 0xffff
    start, end = (0, 0, 0), (length - 1, length - 1)
    stack = [start]

    while stack:
        row, col, cnt = stack.pop()
        if (row, col) == end:
            if ans > cnt:
                ans = cnt

        if cnt < ans and cnt <= ans_list[row][col]:
            for i in range(4):
                nrow, ncol = row + dx[i], col + dy[i]

                if 0 <= nrow < length and 0 <= ncol < length and cnt + route[nrow][ncol] < ans_list[nrow][ncol]:
                    stack.append((nrow, ncol, cnt + route[nrow][ncol]))
                    ans_list[nrow][ncol] = cnt + route[nrow][ncol]

    print("#{} {}".format(tc + 1, ans))