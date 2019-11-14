import sys
sys.stdin = open("17143.txt")

height, width, shark = map(int, input().split())
aquarium = [[0] * width for _ in range(height)]
sharks = [() for _ in range(shark)]

for i in range(shark):
    r, c, s, d, z = map(int, input().split())
    aquarium[r - 1][c - 1] = (s, d, z)
    sharks[i] = (r - 1, c - 1)

answer = 0
for w in range(width):
    for idx in range(shark):
        r, c = sharks[idx]
        if w == r:
            answer += aquarium[r][c][2]
            aquarium[r][c] = 0
            sharks[idx] = (-1, -1)

    for i in range(shark):
        r, c = sharks[i]
        if r >= 0:
