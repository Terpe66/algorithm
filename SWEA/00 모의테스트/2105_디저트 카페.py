import sys
sys.stdin = open("2105.txt")


def find_cafe(r, c, dir, cafe_list):
    global answer

    if answer == (length - 1) * 2:
        return

    if dir == 0:
        if r + 1 < length and c + 1 < length and cafe[r + 1][c + 1] not in cafe_list:
            find_cafe(r + 1, c + 1, 0, cafe_list + [cafe[r + 1][c + 1]])
        if len(cafe_list) > 1 and r + 1 < length and c - 1 >= 0 and cafe[r + 1][c - 1] not in cafe_list:
            find_cafe(r + 1, c - 1, 1, cafe_list + [cafe[r + 1][c - 1]])
    elif dir == 1:
        if r + 1 < length and c - 1 >= 0 and cafe[r + 1][c - 1] not in cafe_list:
            find_cafe(r + 1, c - 1, 1, cafe_list + [cafe[r + 1][c - 1]])
        if r - 1 >= 0 and c - 1 >= 0 and cafe[r - 1][c - 1] not in cafe_list:
            find_cafe(r - 1, c - 1, 2, cafe_list + [cafe[r - 1][c - 1]])
    elif dir == 2:
        if r - 1 >= 0 and c - 1 >= 0 and cafe[r - 1][c - 1] not in cafe_list:
            find_cafe(r - 1, c - 1, 2, cafe_list + [cafe[r - 1][c - 1]])
        if r - 1 >= 0 and c + 1 < length and cafe[r - 1][c + 1] not in cafe_list:
            find_cafe(r - 1, c + 1, 3, cafe_list + [cafe[r - 1][c + 1]])
        if r - 1 == row and c + 1 == col:
            answer = max(answer, len(cafe_list))
    elif dir == 3:
        if r - 1 >= 0 and c + 1 < length and cafe[r - 1][c + 1] not in cafe_list:
            find_cafe(r - 1, c + 1, 3, cafe_list + [cafe[r - 1][c + 1]])
        if r - 1 == row and c + 1 == col:
            answer = max(answer, len(cafe_list))

for T in range(int(input())):
    answer = -1
    length = int(input())
    cafe = [list(map(int, input().split())) for _ in range(length)]

    for row in range(length):
        for col in range(1, length - 1):
            if row == col:
                continue
            find_cafe(row, col, 0, [cafe[row][col]])

    print("#{} {}".format(T + 1, answer))
