import sys
sys.stdin = open("2001.txt")

for t in range(int(input())):
    size, swatter = map(int, input().split())
    wall = []

    for _ in range(size):
        wall.append(list(map(int, input().split())))

    row, col, max_sum = 0, 0, 0
    while row + swatter < size+1:
        while col + swatter < size+1:
            # 5x5, 2x2
            new_sum, ridx, cidx, rng = 0, row, col, col + swatter
            while cidx < rng and ridx < row + swatter:
                new_sum += wall[ridx][cidx]
                cidx += 1
                if cidx == rng:
                    cidx = col
                    ridx += 1
            col += 1
            if max_sum < new_sum:
                max_sum = new_sum
        row += 1
        col = 0

    print(f"#{t+1} {max_sum}")
