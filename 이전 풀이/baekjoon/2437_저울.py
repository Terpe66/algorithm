import sys
sys.stdin = open("2437.txt")

def plus()

N = int(input())
nums = list(map(int, input().split()))
# chk = [0xffffff] * 100000
# chk[0] = -1
#
# for i in range(N):
#     for j in range(100000):
#         if chk[j] < i:
#             if chk[j + nums[i]] == 0xffffff:
#                 chk[j + nums[i]] = i
#
# for j in range(100000):
#     if chk[j] > i:
#         break
#
# print(j)