import sys
sys.stdin = open("1249.txt")


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(int(input())):
    length = int(input())
    route = [list(map(int, input())) for _ in range(length)]
    ans_list = [[0xffff] * length for _ in range(length)]
    stack = [(0, 0)]
    ans_list[0][0] = 0

    while stack:
        row, col = stack.pop(0)
        for i in range(4):
            nrow, ncol = row + dx[i], col + dy[i]
            if 0 <= nrow < length and 0 <= ncol < length and ans_list[row][col] + route[nrow][ncol] < ans_list[nrow][ncol]:
                    ans_list[nrow][ncol] = ans_list[row][col] + route[nrow][ncol]
                    stack.append((nrow, ncol))

    print("#{} {}".format(tc + 1, ans_list[length-1][length-1]))

