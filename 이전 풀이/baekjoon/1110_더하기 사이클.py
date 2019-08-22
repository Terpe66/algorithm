import sys
sys.stdin = open("1110.txt")

for _ in range(3):
    first_num = input()
    cnt = 0
    if len(first_num) == 2:
        sum_num = first_num
    else:
        first_num = "0"+first_num
        sum_num = first_num
    while True:
        sum_num = sum_num[1] + str(int(sum_num[0]) + int(sum_num[1]))[-1]
        cnt += 1
        if sum_num == first_num:
            break
    print(cnt)