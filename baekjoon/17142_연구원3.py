import sys
sys.stdin = open("17142.txt")

N, M = map(int, input().split())
MAP = [[] for _ in range(N)]
Vs = []

for _ in range(N):
    inputs = input().split()
    for i in range(N):
        if inputs[i] == "2":
            Vs.append([_, i])
    MAP[_] = inputs

