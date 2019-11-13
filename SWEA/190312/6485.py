import sys
sys.stdin = open("6485.txt")

for t in range(int(input())):
    N = int(input())

    BUS = []
    for _ in range(N):
        BUS.append(list(map(int, input().split())))

    P = int(input())
    C = []
    for p in range(P):
        C.append(int(input()))

    print(f"#{t+1}", end=" ")
    for c in C:
        cnt = 0
        for b in BUS:
            if b[0] <= c <= b[1]:
                cnt += 1

        print(cnt, end=" ")
    print()

# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     cnt = [0] * 5001
#     for _ in range(N):
#         A, B = map(int, input().split())
#         for i in range(A, B + 1):
#             cnt[i] += 1
#     P = int(input())
#     result = []
#     for _ in range(P):
#         C = int(input())
#         result.append(cnt[C])