import sys
sys.stdin = open("4111.txt")

def light(length = 0, start = 0, end = 1, new = 0):
    global ans
    if length == R:
        if ans > new:
            ans = new
        return

    if length == R - 1:
        i = C - 1
        light(length + 1, end + 1, i, new + (point[i] - point[start]))
    else:
        i = end
        while i < C - 2 * (length + 1):
            light(length + 1, i + 1, i + 2, new + (point[i] - point[start]))
            i += 1

for t in range(int(input())):
    C = int(input())
    R = int(input())
    point = list(set(map(int, input().split())))
    point.sort()
    if C < R:
        print(f"#{t + 1} 0")

    C = len(point)
    # light()
    ans = point[-1] - point[0]
    minus = [point[i + 1] - point[i] for i in range(C - 1)]
    minus.sort(reverse=True)
    for i in range(R - 1):
        ans -= minus[i]

    print(f"#{t + 1} {ans}")

    # 2개 [0, 1, 2, 3, 4]
    # idx 1 : 0, 1, 2
    # idx 2 : 2, 3, 4
    # 1 : start 0, end 2
    # 2 : start 2, end 4

    # 3개 [0, 1, 2, 3, 4, 5, 6]
    # 1 : start 0, end 2
    # 2 : start 2, end 4
    # 3 : start 4, end 6

    # 카메라 개수 // 수신기
    # 2개 [0, 1, 2, 3, 4, 5, 6]
    # 1 : start 0, end 4
    # 2 : start 2, end 6


