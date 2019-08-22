import sys
sys.stdin = open("workshop.txt")

for t in range(int(input())):
    size = int(input())
    HR = []
    for _ in range(size):
        HR.append(input().split())

    visited = [[True]*size for _ in range(size)]
    Q, ans = [], []
    row = 0
    while row < size:
        for col in range(size):
            ridx, cidx = row, col
            if HR[row][col] != "0" and visited[row][col]:
                Q.append((row, col))
                while HR[row][cidx+1] != "0" and visited[row][cidx+1]:
                    cidx += 1

                while HR[ridx+1][cidx] != "0" and visited[ridx+1][cidx]:
                    ridx += 1

                Q.append((ridx, cidx))

                size_point = Q.pop()
                row_size, col_size = size_point[0], size_point[1]
                base_point = Q.pop()
                row_base, col_base = base_point[0], base_point[1]
                ans_point = (size_point[0]-base_point[0]+1, size_point[1]-base_point[1]+1)

                for r in range(row_base, row_size+1):
                    for c in range(col_base, col_size+1):
                        visited[r][c] = False

                ans.append(ans_point)
        row += 1

    ANS = []
    for sna in ans:
        if not ANS:
            ANS.append([0, sna[0]*sna[1], sna[0], sna[1]])
            continue
        cnt = 0
        for SNA in ANS:
            S = sna[0] * sna[1]
            if S > SNA[1]:
                cnt += 1
            elif S == SNA[1] and sna[0] > SNA[2]:
                cnt += 1
        else:
            for SNA in ANS:
                if SNA[0] >= cnt:
                    SNA[0] += 1
            ANS.append([cnt, sna[0]*sna[1], sna[0], sna[1]])

    idx = len(ANS)
    ans = [0] * idx
    for i in range(idx):
        ans[ANS[i][0]] = (ANS[i][2], ANS[i][3])


    print(f"#{t+1} {len(ans)}", end=" ")

    for sna in ans:
        print(sna[0], sna[1], end=" ")
    print()
