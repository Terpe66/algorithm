import sys
sys.stdin = open("4408.txt")

for t in range(int(input())):
    N = int(input())
    room = []
    for _ in range(N):
        x, y = map(int, input().split())
        if y < x:
            x, y = y, x
        room.append((x, y))
    room.sort()
    ans = 0

    bstart = bend = i = 0
    while True:
        start, end = room[i]

        if room == [(0, 0)] * N:
            break

        if start == end == 0:
            i += 1
            if i == N:
                i = 0
            continue

        if not bstart < start < bend and not bstart < end < bend:
            bstart, bend = start, end
            room[i] = (0, 0)
        i += 1

        if i == N:
            bstart = bend = i = 0
            ans += 1


    print(f"#{t + 1} {ans}")