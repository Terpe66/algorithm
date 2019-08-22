import sys
sys.stdin = open("B2636.txt")

width, height = map(int, input().split())
MAP = []
cz_cnt = 0

R_r = [-1, -1, -1, 0, 1, 1, 1, 0]
R_c = [-1, 0, 1, 1, 1, 0, -1, -1]

D_r = [-1, 0, 1, 1, 1, 0, -1, -1]
D_c = [1, 1, 1, 0, -1, -1, -1, 0]

L_r = [1, 1, 1, 0, -1, -1, -1, 0]
L_c = [1, 0, -1, -1, -1, 0, 1, 1]

U_r = [1, 0, -1, -1, -1, 0, 1, 1]
U_c = [-1, -1, -1, 0, 1, 1, 1, 0]

for i in range(height):
    inputs = input().split()
    for j in inputs:
        if j == "1":
            cz_cnt += 1
    MAP.append(inputs)

tmp_cz = cz_cnt

stack = []
while cz_cnt > 0:
    dir = "R"
    for row in range(height):
        for col in range(width):
            if MAP[row][col] == "1":
                stack.append((row, col))
                while stack:
                    s_row, s_col = stack.pop()

                    if dir == "R":
                        for i in range(8):
                            d_row, d_col = D_r[i] + s_row, D_c[i] + s_col

                            if 0 <= d_row < height and 0 <= d_col < width and MAP[d_row][d_col] == "1":
                                stack.append((d_row, d_col))
                                break





    if cz_cnt != 0:
        tmp_cz = cz_cnt


