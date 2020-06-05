import sys
sys.stdin = open("5648.txt")


for T in range(int(input())):
    answer = 0
    N = int(input())
    atom = [list(map(int, input().split())) for _ in range(N)]
    lives = [0] * N
    check_atom = {}

    for i in range(N):
        x, y, d, k = atom[i]
        for j in range(i + 1, N):
            nx, ny, nd, nk = atom[j]
            chk = False
            if x == nx:
                if d == 0 and nd == 1 and y < ny or d == 1 and nd == 0 and y > ny:
                    key = abs(ny - y) / 2
                    chk = True
            elif y == ny:
                if d == 2 and nd == 3 and x > nx or d == 3 and nd == 2 and x < nx:
                    key = abs(nx - x) / 2
                    chk = True
            elif abs(x - nx) == abs(y - ny):
                if d == 0:
                    if nd == 3 and x > nx and y < ny or nd == 2 and x < nx and y < ny:
                        key = abs(x - nx)
                        chk = True
                elif d == 1:
                    if nd == 3 and x > nx and y > ny or nd == 2 and x < nx and y > ny:
                        key = abs(x - nx)
                        chk = True
                elif d == 2:
                    if nd == 0 and x > nx and y > ny or nd == 1 and x > nx and y < ny:
                        key = abs(x - nx)
                        chk = True
                elif d == 3:
                    if nd == 0 and x < nx and y > ny or nd == 1 and x < nx and y < ny:
                        key = abs(x - nx)
                        chk = True
            if chk:
                check_atom.setdefault(key, []).append((i, j))
                lives[i] = lives[j] = 1

    keys = sorted(check_atom.keys())
    for key in keys:
        tmp = set()
        for val in check_atom[key]:
            a, b = val
            if lives[a] and lives[b]:
                tmp.add(a)
                tmp.add(b)
        for i in tmp:
            lives[i] = 0
            answer += atom[i][3]

    print("#{} {}".format(T + 1, answer))
