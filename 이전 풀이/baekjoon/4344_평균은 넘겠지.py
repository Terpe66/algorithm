import sys
sys.stdin = open("4344.txt")

for T in range(int(input())):
    inputs = list(map(int, input().split()))
    N, inputs = inputs[0], inputs[1:]
    avg = sum(inputs) / N
    cnt = 0
    for p in inputs:
        if p > avg:
            cnt += 1
    avg_p = str(round(cnt / N * 100, 3))
    # ans = str(avg_p)[-1:-4:-1] + "." + str(avg_p)[-4::-1]

    # print(f"{ans[::-1]}%")
    for i in range(len(avg_p)):
        if avg_p[i] == ".":
            break
    length = len(avg_p[i+1:])
    if length == 2:
        avg_p += "0"
    elif length == 1:
        avg_p += "00"

    print(f"{avg_p}%")