import sys
sys.stdin = open("workshop.txt")

def math(start):
    if not leaf[start]:
        return node[start]
    a = math(leaf[start][0])
    b = math(leaf[start][1])
    if node[start] == "+":
        return a + b
    if node[start] == "-":
        return a - b
    if node[start] == "*":
        return a * b
    if node[start] == "/":
        return a // b

for t in range(10):
    N = int(input())
    leaf = [[] for _ in range(N + 1)]
    node = [0] * (N + 1)

    for i in range(N):
        inputs = list(map(str, input().split()))
        idx = int(inputs[0])
        if len(inputs) > 2:
            node[idx] = inputs[1]
            leaf[idx].append(int(inputs[2]))
            leaf[idx].append(int(inputs[3]))
        else:
            node[idx] = int(inputs[1])

    print(f"#{t+1} {math(1)}")