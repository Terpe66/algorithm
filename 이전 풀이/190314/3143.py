import sys
sys.stdin = open("3143.txt")

for t in range(int(input())):
    # string : 검사해야 하는 글자, fn : 단축 글자
    string, fn = input().split()
    idx = cnt = 0
    # fn_idx : 단축 글자와 동일한지 탐색, 맞으면 이동시켜줄 index 변수, max_idx : 검사해야 하는 글자의 최대 길이(탐색 길이)
    fn_idx, max_idx = len(fn), len(string)
    # 탐색하는 index(idx)가 최대 길이를 넘지 않으면 반복문 진행(넘어가면 탈줄)
    while idx < max_idx:
        # idx + fn_idx - 1 : 현재 index부터 단축 글자의 글자수만큼의 거리가 최대 길이를 넘어서면 더 탐색할 필요가 없기 때문에 진입
        if idx + fn_idx - 1 > max_idx:
            # cnt에 남은 글자수를 더하고 반복문 탈출
            cnt += len(string[idx:])
            break
        # 검사해야 하는 글자의 현재 index부터 단축 글자의 글자수만큼이 단축 글자와 동일하면 진입
        if string[idx:idx + fn_idx] == fn:
            # 현재 index를 단축 글자수만큼 뒤로 이동시켜준다
            idx += fn_idx
            cnt += 1
            continue
        # 모두 해당하지 않으면 한 글자씩 입력하는 것이기 때문에 cnt와 idx를 각각 1씩 증가
        cnt += 1
        idx += 1

    print(f"#{t + 1} {cnt}")