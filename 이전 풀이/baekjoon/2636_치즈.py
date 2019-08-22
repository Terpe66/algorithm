import sys
sys.stdin = open("2636.txt")

R, C = map(int, input().split())
pizza = []

for _ in range(R):
    pizza.append(input().split())

visited = [[True] * C for _ in range(R)]
S = []
row = col = 0
while row < R:
    while col < C:
        ridx, cidx = row, col
        if pizza[row][col] == "0":
            visited[row][col] = False
            col += 1
            continue

        if pizza[row][col]


        while cidx + 1 < C and ridx + 1 < R and visited[row][col]:
            S.append((ridx, cidx))

            if pizza[ridx - 1][cidx] == "1" and pizza[ridx - 1][cidx - 1] == "0" and visited[ridx - 1][cidx]:
                visited[ridx - 1][cidx] = False
                ridx -= 1

            elif pizza[ridx - 1][cidx + 1] == "1" and pizza[ridx - 1][cidx] == "0" and visited[ridx - 1][cidx + 1]:
                visited[ridx - 1][cidx + 1] = False
                ridx -= 1
                cidx += 1

            elif pizza[ridx][cidx + 1] == "1" and pizza[ridx - 1][cidx + 1] == "0"and visited[ridx][cidx + 1]:
                visited[ridx][cidx + 1] = False
                cidx += 1

            elif pizza[ridx + 1][cidx + 1] == "1" and pizza[ridx][cidx + 1] == "0" and visited[ridx + 1][cidx + 1]:
                visited[ridx + 1][cidx + 1] = False
                ridx += 1
                cidx += 1

            elif pizza[ridx + 1][cidx] == "1" and visited[ridx + 1][cidx]:
                visited[ridx + 1][cidx] = False
                ridx += 1

            elif pizza[ridx + 1][cidx - 1] == "1" and visited[ridx + 1][cidx - 1]:
                visited[ridx + 1][cidx - 1] = False
                ridx += 1
                cidx -= 1

            elif pizza[ridx][cidx - 1] == "1" and visited[ridx][cidx - 1]:
                visited[ridx][cidx - 1] = False
                cidx -= 1

            elif pizza[ridx - 1][cidx - 1] == "1" and visited[ridx - 1][cidx - 1]:
                visited[ridx - 1][cidx - 1] = False
                ridx -= 1
                cidx -= 1

        col += 1

    col = 0
    row += 1






print(pizza)
print(visited)