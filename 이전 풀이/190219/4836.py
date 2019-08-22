import sys
sys.stdin = open("4836.txt", "r")

for T in range(int(input())):
    paint_list = []
    empty_list = []
    for e in range(10):
        empty_list.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    for c in range(int(input())):
        paint_list.append(list(map(int, input().split())))
    for paint in paint_list:
        for i in range(paint[0], paint[2]+1):
            for j in range(paint[1], paint[3]+1):
                empty_list[i][j] += paint[4]
    cnt = 0
    for c in empty_list:
        cnt += c.count(3)
    print("#{} {}".format(T+1, cnt))