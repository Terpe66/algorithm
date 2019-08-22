import sys
sys.stdin = open("17135.txt")


def reset():

    for row, col in enemy_position:
        Map[row][col] = "1"


def bow(cnt):

    if cnt == 0:
        for i in range(width):
            if Map[height][i] == "S":
                bow_position.append((height, i))
        return

    for i in range(width):
        if Map[height][i] == "0":
            Map[height][i] = "S"
            bow(cnt - 1)
            Map[height][i] = "0"


def kill():

    for i in range(3):
        row, col = bow_position[i]
        r, c = row, col

        R = 0
        while height - R > 0:

            for ran in range(1, rng + 1):
                nr, nc = r, c - ran
                mr, mc = r - ran, c + ran

                while nr >= r:
                    if 0 <= nr < height and 0 <= nc < width: # and
                        pass


height, width, rng = map(int, input().split())
Map = []
enemy_position = []
bow_position = []
for _ in range(height):
    inputs = input().split()
    for i in range(width):
        if inputs[i] == "1":
            enemy_position.append((_, i))
    Map.append(inputs)

Map.append(["0"] * width)


