import sys
sys.stdin = open("5108.txt")

for t in range(int(input())):
    suyul, plus, idx = map(int, input().split())
    S = input().split()
    plus_idx = []
    S += [""] * plus
    for _ in range(plus):
        plus_idx.append(input().split())

    while plus_idx:
        index = len(plus_idx)
        pop = plus_idx.pop(0)

        for i in range(len(S)-1-index, int(pop[0])-2, -1):
            S[i+1] = S[i]

        S[int(pop[0])] = pop[1]

    print(f"#{t+1} {S[idx]}")