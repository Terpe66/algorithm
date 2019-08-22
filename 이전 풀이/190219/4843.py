import sys
sys.stdin = open("4839.txt", "r")

for T in range(int(input())):
    length = int(input())
    num_list = list(map(int, input().split()))
    for i in range(length):
        max_n, max_i = num_list[i], i
        min_n, min_i = num_list[i], i
        if i % 2 == 0:
            for j in range(i+1, length):
                if num_list[j] > max_n:
                    max_n = num_list[j]
                    max_i = j
            num_list[i], num_list[max_i] = max_n, num_list[i]
        else:
            for j in range(i+1, length):
                if num_list[j] < min_n:
                    min_n = num_list[j]
                    min_i = j
            num_list[i], num_list[min_i] = min_n, num_list[i]
    print("#{}".format(T+1), end=" ")
    for i in range(10):
        if i < 9:
            print(num_list[i], end=" ")
        else:
            print(num_list[i])