import sys
sys.stdin = open("5650.txt")

from collections import deque

for t in range(int(input())):
    size = int(input())
    board = [input().split() for _ in range(size)]
    worm = [[] for _ in range(11)]
    D = []
    ans = 0
    for row in range(size):
        for col in range(size):
            if board[row][col] in ("6", "7", "8", "9", "10"):
                worm[int(board[row][col])].append((row, col))

    for row in range(size):
        for col in range(size):
            if board[row][col] == "0":
                if row == 0 or board[row - 1][col] in ("1", "2", "3", "4", "5"):
                    D.append("d")
                if row == size - 1 or board[row + 1][col] in ("1", "2", "3", "4", "5"):
                    D.append("u")
                if col == 0 or board[row][col - 1] in ("1", "2", "3", "4", "5"):
                    D.append("r")
                if col == size - 1 or board[row][col + 1] in ("1", "2", "3", "4", "5"):
                    D.append("l")

                while D:
                    r, c, cnt, chk, dir = row, col, 0, False, D.pop()

                    if dir == "u":
                        r -= 1
                    elif dir == "r":
                        c += 1
                    elif dir == "d":
                        r += 1
                    elif dir == "l":
                        c -= 1

                    while chk == False:

                        while dir == "u":
                            if r < 0:
                                r = 0
                                cnt += 1
                                dir = "d"
                            elif board[r][c] == "1" or board[r][c] == "4" or board[r][c] == "5":
                                cnt += 1
                                r += 1
                                dir = "d"
                            elif board[r][c] == "2":
                                cnt += 1
                                c, dir = c + 1, "r"
                            elif board[r][c] == "3":
                                cnt += 1
                                c, dir = c - 1, "l"
                            elif board[r][c] in ("6", "7", "8", "9", "10"):
                                idx = int(board[r][c])
                                if worm[idx][0] == (r, c):
                                    r, c = worm[idx][1]
                                else:
                                    r, c = worm[idx][0]
                                r -= 1
                            elif board[r][c] == "-1" or (r, c) == (row, col):
                                chk = True
                                break
                            else:
                                r -= 1

                        while dir == "d":
                            if r > size - 1:
                                r = size - 1
                                cnt += 1
                                dir = "u"
                            elif board[r][c] == "1":
                                cnt += 1
                                c, dir = c + 1, "r"
                            elif board[r][c] == "2" or board[r][c] == "3" or board[r][c] == "5":
                                cnt += 1
                                r -= 1
                                dir = "u"
                            elif board[r][c] == "4":
                                cnt += 1
                                c, dir = c - 1, "l"
                            elif board[r][c] in ("6", "7", "8", "9", "10"):
                                idx = int(board[r][c])
                                if worm[idx][0] == (r, c):
                                    r, c = worm[idx][1]
                                else:
                                    r, c = worm[idx][0]
                                r += 1
                            elif board[r][c] == "-1" or (r, c) == (row, col):
                                chk = True
                                break
                            else:
                                r += 1

                        while dir == "l":
                            if c < 0:
                                c = 0
                                cnt += 1
                                dir = "r"
                            elif board[r][c] == "3" or board[r][c] == "4" or board[r][c] == "5":
                                cnt += 1
                                c += 1
                                dir = "r"
                            elif board[r][c] == "2":
                                cnt += 1
                                r, dir = r + 1, "d"
                            elif board[r][c] == "1":
                                r, dir = r - 1, "u"
                                cnt += 1
                            elif board[r][c] in ("6", "7", "8", "9", "10"):
                                idx = int(board[r][c])
                                if worm[idx][0] == (r, c):
                                    r, c = worm[idx][1]
                                else:
                                    r, c = worm[idx][0]
                                c -= 1
                            elif board[r][c] == "-1" or (r, c) == (row, col):
                                chk = True
                                break
                            else:
                                c -= 1

                        while dir == "r":
                            if c > size - 1:
                                c = size - 1
                                cnt += 1
                                dir = "l"
                            elif board[r][c] == "1" or board[r][c] == "2" or board[r][c] == "5":
                                cnt += 1
                                c -= 1
                                dir = "l"
                            elif board[r][c] == "3":
                                cnt += 1
                                r, dir = r + 1, "d"
                            elif board[r][c] == "4":
                                cnt += 1
                                r, dir = r - 1, "u"
                            elif board[r][c] in ("6", "7", "8", "9", "10"):
                                idx = int(board[r][c])
                                if worm[idx][0] == (r, c):
                                    r, c = worm[idx][1]
                                else:
                                    r, c = worm[idx][0]
                                c += 1
                            elif board[r][c] == "-1" or (r, c) == (row, col):
                                chk = True
                                break
                            else:
                                c += 1

                    if ans < cnt:
                        ans = cnt





                # if i == 0 or board[i - 1][j] == "1" or board[i - 1][j] == "4" or board[i - 1][j] == "5":
                #     Q.append((i, j, "d"))
                # if j == 0 or board[i][j - 1] == "3" or board[i][j - 1] == "4" or board[i][j - 1] == "5":
                #     Q.append((i, j, "r"))
                # if i == size - 1 or board[i + 1][j] == "2" or board[i + 1][j] == "3" or board[i + 1][j] == "5":
                #     Q.append((i, j, "u"))
                # if j == size - 1 or board[i][j + 1] == "1" or board[i][j + 1] == "2" or board[i][j + 1] == "5":
                #     Q.append((i, j, "l"))

    #         elif board[i][j] in ("6", "7", "8", "9", "10"):
    #             worm[int(board[i][j])].append((i, j))
    #
    # while Q:
    #     row, col, dir = Q.popleft()
    #     r, c, cnt, chk = row, col, 0, False
    #
    #     if dir == "u":
    #         r -= 1
    #     elif dir == "r":
    #         c += 1
    #     elif dir == "d":
    #         r += 1
    #     elif dir == "l":
    #         c -= 1
    #
    #     while chk == False:
    #
    #         while dir == "u":
    #             if r < 0:
    #                 r = 0
    #                 cnt += 1
    #                 dir = "d"
    #                 if (r, c, dir) in Q:
    #                     Q.remove((r, c, dir))
    #             elif board[r][c] == "1" or board[r][c] == "4" or board[r][c] == "5":
    #                 cnt += 1
    #                 r += 1
    #                 dir = "d"
    #                 if (r, c, dir) in Q:
    #                     Q.remove((r, c, dir))
    #             elif board[r][c] == "2":
    #                 cnt += 1
    #                 c, dir = c + 1, "r"
    #             elif board[r][c] == "3":
    #                 cnt += 1
    #                 c, dir = c - 1, "l"
    #             elif board[r][c] in ("6", "7", "8", "9", "10"):
    #                 idx = int(board[r][c])
    #                 if worm[idx][0] == (r, c):
    #                     r, c = worm[idx][1]
    #                 else:
    #                     r, c = worm[idx][0]
    #                 r -= 1
    #             elif board[r][c] == "-1" or (r, c) == (row, col):
    #                 chk = True
    #                 break
    #             else:
    #                 r -= 1
    #
    #         while dir == "d":
    #             if r > size - 1:
    #                 r = size - 1
    #                 cnt += 1
    #                 dir = "u"
    #                 if (r, c, dir) in Q:
    #                     Q.remove((r, c, dir))
    #             elif board[r][c] == "1":
    #                 cnt += 1
    #                 c, dir = c + 1, "r"
    #             elif board[r][c] == "2" or board[r][c] == "3" or board[r][c] == "5":
    #                 cnt += 1
    #                 r -= 1
    #                 dir = "u"
    #                 if (r, c, dir) in Q:
    #                     Q.remove((r, c, dir))
    #             elif board[r][c] == "4":
    #                 cnt += 1
    #                 c, dir = c - 1, "l"
    #             elif board[r][c] in ("6", "7", "8", "9", "10"):
    #                 idx = int(board[r][c])
    #                 if worm[idx][0] == (r, c):
    #                     r, c = worm[idx][1]
    #                 else:
    #                     r, c = worm[idx][0]
    #                 r += 1
    #             elif board[r][c] == "-1" or (r, c) == (row, col):
    #                 chk = True
    #                 break
    #             else:
    #                 r += 1
    #
    #         while dir == "l":
    #             if c < 0:
    #                 c = 0
    #                 cnt += 1
    #                 dir = "r"
    #                 if (r, c, dir) in Q:
    #                     Q.remove((r, c, dir))
    #             elif board[r][c] == "3" or board[r][c] == "4" or board[r][c] == "5":
    #                 cnt += 1
    #                 c += 1
    #                 dir = "r"
    #                 if (r, c, dir) in Q:
    #                     Q.remove((r, c, dir))
    #             elif board[r][c] == "2":
    #                 cnt += 1
    #                 r, dir = r + 1, "d"
    #             elif board[r][c] == "1":
    #                 r, dir = r - 1, "u"
    #                 cnt += 1
    #             elif board[r][c] in ("6", "7", "8", "9", "10"):
    #                 idx = int(board[r][c])
    #                 if worm[idx][0] == (r, c):
    #                     r, c = worm[idx][1]
    #                 else:
    #                     r, c = worm[idx][0]
    #                 c -= 1
    #             elif board[r][c] == "-1" or (r, c) == (row, col):
    #                 chk = True
    #                 break
    #             else:
    #                 c -= 1
    #
    #         while dir == "r":
    #             if c > size - 1:
    #                 c = size - 1
    #                 cnt += 1
    #                 dir = "l"
    #                 if (r, c, dir) in Q:
    #                     Q.remove((r, c, dir))
    #             elif board[r][c] == "1" or board[r][c] == "2" or board[r][c] == "5":
    #                 cnt += 1
    #                 c -= 1
    #                 dir = "l"
    #                 if (r, c, dir) in Q:
    #                     Q.remove((r, c, dir))
    #             elif board[r][c] == "3":
    #                 cnt += 1
    #                 r, dir = r + 1, "d"
    #             elif board[r][c] == "4":
    #                 cnt += 1
    #                 r, dir = r - 1, "u"
    #             elif board[r][c] in ("6", "7", "8", "9", "10"):
    #                 idx = int(board[r][c])
    #                 if worm[idx][0] == (r, c):
    #                     r, c = worm[idx][1]
    #                 else:
    #                     r, c = worm[idx][0]
    #                 c += 1
    #             elif board[r][c] == "-1" or (r, c) == (row, col):
    #                 chk = True
    #                 break
    #             else:
    #                 c += 1
    #
    #     if ans < cnt:
    #         ans = cnt

    print(f"#{t + 1} {ans}")