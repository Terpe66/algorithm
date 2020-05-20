import sys
sys.stdin = open("16234.txt")


dir = [1, -1, 0, 0]

for T in range(int(input())):
    answer = 0
    length, L, R = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(length)]
    tempBoard = [[0] * length for _ in range(length)]

    chk = True
    while chk:
        chk = False
        for row in range(length):
            for col in range(length):
                if tempBoard[row][col] == 0:
                    empty = set()
                    empty.add((row, col))
                    temp = [(row, col)]
                    point = board[row][col]
                    count = 0
                    while temp:
                        r, c = temp.pop()

                        for i in range(4):
                            nr, nc = r + dir[i], c + dir[3 - i]
                            if 0 <= nr < length and 0 <= nc < length and L <= abs(board[r][c] - board[nr][nc]) <= R and (nr, nc) not in empty:
                                chk = True
                                point += board[nr][nc]
                                count += 1
                                temp.append((nr, nc))
                                empty.add((nr, nc))

                    if not chk or not count:
                        continue

                    new = point // (count + 1)

                    for r, c in empty:
                        tempBoard[r][c] = new

        if chk:
            answer += 1
            for r in range(length):
                for c in range(length):
                    if tempBoard[r][c]:
                        board[r][c] = tempBoard[r][c]
                        tempBoard[r][c] = 0

    print(answer)