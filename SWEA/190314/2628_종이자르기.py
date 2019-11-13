import sys
sys.stdin = open("2628.txt")

width, height = map(int, input().split())
W, H = [0], [0]
for _ in range(int(input())):
    dir, idx = map(int, input().split())
    if dir:
        W.append(idx)
        continue
    H.append(idx)
W.sort()
H.sort()
W.append(width)
H.append(height)

ans = 0
for w in range(1, len(W)):
    for h in range(1, len(H)):
        now = (W[w - 1] - W[w]) * (H[h - 1] - H[h])
        if ans < now:
            ans = now

print(ans)