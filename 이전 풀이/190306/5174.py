import sys
sys.stdin = open("5174.txt")

def nodecount(start):
    global cnt
    cnt += 1
    if not node[start]:
        return
    for new in node[start]:
        nodecount(new)

for t in range(int(input())):
    line, start = map(int, input().split())
    node = [[] for _ in range(line+2)]
    P = [0] * line
    inputs = list(map(int, input().split()))
    for i in range(0, line*2, 2):
        node[inputs[i]].append(inputs[i+1])

    cnt = 0
    nodecount(start)
    print(f"#{t+1} {cnt}")