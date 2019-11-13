import sys
sys.stdin = open("4008.txt")

def calc(idx, new):

    if idx == N:
        if ans[0] < new:
            ans[0] = new
        if ans[1] > new:
            ans[1] = new
        return

    for i in range(4):
        if tools[i]:
            tools[i] -= 1
            if i == 0:
                calc(idx + 1, new + nums[idx + 1])
            elif i == 1:
                calc(idx + 1, new - nums[idx + 1])
            elif i == 2:
                calc(idx + 1, new * nums[idx + 1])
            elif i == 3:
                if new < 0:
                    calc(idx + 1, - (-new // nums[idx + 1]))
                else:
                    calc(idx + 1, new // nums[idx + 1])
            tools[i] += 1

for t in range(int(input())):
    N = int(input()) - 1
    tools = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    ans = [-100000001, 100000001]

    calc(0, nums[0])

    print(f"#{t + 1} {ans[0] - ans[1]}")