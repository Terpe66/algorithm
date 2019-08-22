import sys
sys.stdin = open("17144.txt")

height, width, T = map(int, input().split())
dust = []
cleaner = []
MAP = []
for i in range(height):
    inputs = list(map(int, input().split()))
    for j in range(width):
        if inputs[j] not in (0, -1):
            dust.append((i, j))

        elif inputs[j] == -1:
            cleaner.append((i, j))
    MAP.append(inputs)

print(MAP)
print(dust)
print(cleaner)