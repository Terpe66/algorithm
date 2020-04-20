import sys
sys.stdin = open("5207.txt")

for t in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 0
    L, R = 0, N - 1
    mid = (L + R) // 2
    for i in range(M):
        l, r, m = L, R, mid
        chk = set()
        while l != r and A[m] != B[i]:
            if B[i] < A[m]:
                r = m - 1
                chk.add("l")
            elif B[i] > A[m]:
                l = m + 1
                chk.add("r")
            m = (l + r) // 2
        if A[m] == B[i]:
            ans += 1

    print(f"#{t + 1} {ans}")