import sys
sys.stdin = open("6190.txt")

for t in range(int(input())):
    N = int(input())
    danjo = list(map(int, input().split()))

    idx, sidx, ans = 0, 1, 0
    while idx < N-1:
        while sidx < N:
            new = str(danjo[idx] * danjo[sidx])
            new_n = len(new)
            stidx, sstidx = 0, 1
            if new_n > 1:
                while stidx < new_n-1:
                    while sstidx < new_n:
                        if new[stidx] <= new[sstidx]:
                            stidx += 1
                            sstidx += 1
                        else:
                            new, stidx = 0, new_n
                            break
                new = int(new)
                if ans < new:
                    ans = new

            sidx += 1
        idx += 1
        sidx = idx + 1

    if ans:
        print(f"#{t+1} {ans}")
        continue
    print(f"#{t+1} -1")
