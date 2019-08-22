import sys
sys.stdin = open("4837.txt", "r")

def a(n):
    if n == 0:
        return 0
    return a(n-1) + n

def bubun(n, k, sum_num=0):
    global K, ans
    sum_num += n
    k -= 1
    n += 1

    if sum_num == K and k == 0:
        ans += 1
        return

    if sum_num > K:
        return

    if k > 0:
        while n < 13:
            bubun(n, k, sum_num)
            n += 1

def bubun_ddongle(A, i, k, target_sum):
    if k == 1:
        for j in range(i, len(A)):
            if A[j] == target_sum:
                return 1
        return 0

    cnt = 0
    for j in range(i, len(A)):
        cnt += bubun_ddongle(A, j + 1, k - 1, target_sum - A[j])
    return cnt

for t in range(int(input())):
    N, K = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    sum_list = []

    ans = 0
    for i in A:
        bubun(i, N)


    print(f"#{t+1} {ans}")
