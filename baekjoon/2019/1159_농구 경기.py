import sys
sys.stdin = open("1159.txt")

players = []
for _ in range(int(input())):
    players.append(input())

last = {}
for player in players:
    p = player[0]
    if p in last:
        last[p] += 1
    else:
        last[p] = 1

ans = []
for key, val in last.items():
    if val >= 5:
        ans.append(key)

ans.sort()
if len(ans) > 0:
    print("".join(ans))
else:
    print("PREDAJA")