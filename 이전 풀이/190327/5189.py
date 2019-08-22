import sys
sys.stdin = open("5189.txt")

def find(i, new, chk_i, chk_j):
    global size, ans

    if i == 0:
        if chk_i == [True] * size and new < ans:
            ans = new
        return

    j = 0
    while j < size:
        if chk_i[i] == False and chk_j[j] == False and board[i][j]:
            chk_i[i] = chk_j[j] = True
            find(j, new + board[i][j], chk_i, chk_j)
            chk_i[i] = chk_j[j] = False
        if j == 0 and chk_i == [True] * size:
            chk_i[j] = chk_j[j] = True
            find(j, new + board[i][j], chk_i, chk_j)
            chk_i[j] = chk_j[j] = False
        j += 1

for t in range(int(input())):
    size = int(input())
    board = [list(map(int, input().split())) for _ in range(size)]
    n = 1
    for i in range(1, size + 1):
        n *= i
    chk_i = [False] * size
    chk_j = [False] * size
    ans = 1000

    for i in range(size):
        if board[0][i]:
            chk_j[i] = chk_i[0] = True
            find(i, board[0][i], chk_i, chk_j)
            chk_j[i] = False

    print(f"#{t + 1} {ans}")