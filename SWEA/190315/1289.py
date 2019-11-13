import sys
sys.stdin = open("1289.txt")

for t in range(int(input())):
    base = input()

    # 1) 공식?을 이용해서 세는 방법
    # 가장 왼쪽에 있는 1부터 1씩 숫자를 센다.
    # 연속된 숫자일 경우 숫자를 1만 센다.
    # 참고) 이전에 풀었던 단축 글자 문제

    # 0011일 때, 가장 왼쪽의 1에서 시작하면 연속된 있는 숫자인 11은 하나로 세기 때문에 1
    # 100일 때, 가장 왼쪽의 1 이후 00이 연속된 숫자이기 때문에 하나로 세서 합이 2
    # 01010일 때, 가장 왼쪽의 1 이후 각각 다른 숫자이기 때문에 합이 4

    # 비교 순서가 현재 위치에서 오른쪽에 있는 숫자를 세는 것이기 때문에 ans는 1인 상태로 시작
    idx, ans = 0, 1
    # 가장 왼쪽부터 탐색할 때 0인 경우는 모두 건너야 하고, 그 작업을 위한 반복문
    while base[idx] == "0":
        idx += 1
    # 0이 아닌 위치에서부터 끝 범위의 하나 전까지(오른쪽에 있는 숫자를 세기 때문에)
    for i in range(idx, len(base)-1):
        # 숫자가 다를 경우 ans를 하나 증가
        if base[i] != base[i+1]:
            ans += 1

    print(f"#{t + 1} {ans}")



    # 2) 리스트의 값을 변경해가면서 숫자를 세는 방법
    length = len(base)
    bit = ["0"] * length
    for i in range(length):
        # 같은 위치의 숫자가 다를 경우 진입
        if base[i] != bit[i]:
            # 현재 범위에서부터 뒤의 숫자를 모두 바꾸는 반복문
            for j in range(i, length):
                if bit[j] == "1":
                    bit[j] = "0"
                else:
                    bit[j] = "1"
            ans += 1
    print(f"#{t + 1} {ans}")
