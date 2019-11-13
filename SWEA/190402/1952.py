import sys
sys.stdin = open("1952.txt")

def swim(i = 0, new = 0):
    global ans

    if i >= 12:
        if ans > new:
            ans = new
        return

    if i < 12 and Ms[i]:
        swim(i + 3, new + months)
    swim(i + 1, new + M[i])

for t in range(int(input())):
    day, month, months, ans = map(int, input().split())
    plan = list(map(int, input().split()))

    M = [0] * 12
    Ms = [False] * 12
    for i in range(12):
        if plan[i]:
            if plan[i] * day > month:
                M[i] = month
                continue
            M[i] = plan[i] * day

    for i in range(12):
        if M[i]:
            j, new = i, 0
            while j < 12 and j < i + 3:
                new += M[j]
                j += 1
            if new > months:
                Ms[i] = True

    for i in range(12):
        if M[i]:
            swim(i)
            break

    print(f"#{t + 1} {ans}")