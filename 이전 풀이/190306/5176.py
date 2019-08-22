import sys
sys.stdin = open("5176.txt")

def find(start):
    global root, ans, cnt
    if not node[start]:
        cnt += 1
    elif node[start][0]:
        find(node[start][0])
        cnt += 1
    if start == 1 and cnt:
        root = cnt
    if start == N//2 and cnt:
        ans = cnt
    if len(node[start]) == 2:
        find(node[start][1])

for t in range(int(input())):
    N = int(input())
    node = [ [] for _ in range(N+1)]

    for i in range(2, N+1):
        node[i//2].append(i)

    root, ans, cnt = 0, 0, 0
    find(1)

    print(f"#{t+1} {root} {ans}")