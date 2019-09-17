dr, dc = [-1, 1, 0, 0], [0, 0, 1, -1]


def solution(m, n, puddles):
    answer = 0
    up = row = col = 1

    for i in range(m + n - 2, 1, -1):
        up *= i
        if i <= m - 1:
            col *= i
        if i <= n - 1:
            row *= i

    answer = up // (row * col)

    for nn, nm in puddles:
        nup = nrow = ncol = 1
        for i in range(nm + nn - 2, 1, -1):
            nup *= i
            if i <= nm - 1:
                ncol *= i
            if i <= nn - 1:
                nrow *= i
        a = nup // (nrow * ncol)

        nup = nrow = ncol = 1
        for i in range(n - nn + m - nm, 1, -1):
            nup *= i
            if i <= m - nm:
                ncol *= i
            if i <= n - nn:
                nrow *= i
        b = nup // (nrow * ncol)

        answer = (answer - a * b) % 1000000007

    return answer

solution(4, 3, [[2, 2], [2, 3]])