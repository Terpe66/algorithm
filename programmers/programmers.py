dr, dc = [1, 0], [0, 1]


def solution(width, height, puddles):
    answer = 0
    MAP = [[0] * width for _ in range(height)]

    for r, c in puddles:
        MAP[r - 1][c - 1] = 1

    q = [(0, 0)]
    while q:
        row, col = q.pop(0)
        if (row, col) == (height - 1, width - 1):
            answer += 1

        for i in range(2):
            nrow, ncol = row + dr[i], col + dc[i]
            if 0 <= nrow < height and 0 <= ncol < width and MAP[nrow][ncol] == 0:
                q.append((nrow, ncol))

    return answer

solution(4, 3, [[2, 2]])