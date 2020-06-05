import sys
sys.stdin = open("4012.txt")

import itertools


for T in range(int(input())):
    answer = 0xffffffff
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    iter_list = list(itertools.combinations([i for i in range(N)], N // 2))

    for i in range(len(iter_list) // 2):
        temp1 = iter_list[i]
        temp2 = iter_list[i * -1 - 1]
        point = 0
        for j in range(N // 2):
            for k in range(j + 1, N // 2):
                point = point + (board[temp1[j]][temp1[k]] + board[temp1[k]][temp1[j]]) - (board[temp2[j]][temp2[k]] + board[temp2[k]][temp2[j]])

        answer = min(answer, abs(point))

    print("#{} {}".format(T + 1, answer))
