T = int(input())

for t in range(T):
    data = []
    N, M = map(int, input().split())
    j = 0
    result = False

    for n in range(N):
        data.append(list(input()))

    for j in range(N):
        n, m, count = 0, 1, 0
        while n+M-m < N:
            if data[j][n] == data[j][n+M-m]:
                m = m + 2
                count += 1
                if count == M//2:
                    print(f"#{t+1}", end=" ")
                    for i in range(n-M//2+1, (n-M//2+1)+M):
                        print(data[j][i], end="")
                    print()
                    result = True
                    break
            else:
                m = 1
                n -= count
                count = 0
            n = n + 1

    result = False
    if result == False:
        for j in range(N):
            n, m, count = 0, 1, 0
            while n+M-m < N:
                if data[n][j] == data[n+M-m][j]:
                    m = m + 2
                    count += 1
                    if count == M//2:
                        print(f"#{t+1}", end=" ")
                        for i in range(n-M//2+1, (n-M//2+1)+M):
                            print(data[i][j], end="")
                        print()
                        break
                else:
                    m = 1
                    n -= count
                    count = 0
                n = n + 1
