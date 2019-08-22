import sys
sys.stdin = open("2007.txt")

for t in range(int(input())):
    input_string = input()
    max_idx = len(input_string)
    idx = i = 0
    string = ""
    while idx < max_idx and i < 10:
        string += input_string[i]
        for n in range(i + 1, 20, i + 1):
            if string != input_string[n:n + i + 1]:
                break
        else:
            print(f"#{t + 1} {len(string)}")
            break
        i += 1
    continue

    # i : 탐색하기 위한 변수
    i = 1
    # input_string의 첫 글자와 반복이 끝나는 지점 탐색
    while i < 10 and input_string[0] == input_string[i]:
        i += 1
    # 반복이 끝나는 지점까지 string으로 설정
    string = input_string[:i]
    while i < max_idx:
        compare = input_string[i]
        # string의 첫 글자와 input_string의 i번째 글자 비교
        # SAMSUNG일 땐 string은 S, input_string[i]는 A
        if string[0] != compare:
            # 만약 두 글자가 다르면 string에 글자를 추가
            # string == SA
            # 반복되면 SAM까지 등록됨
            string += compare
        else:
            for n in range(len(string)):
                # string의 n번째 글자와 input_string의 i번째 글자가 같으면 계속 진행
                if string[n] == input_string[i]:
                    i += 1
                else:
                    # 만약 다른 경우엔 string을 처음부터 i번째 글자까지로 변경
                    string = input_string[:i+1]
                    break
            # for문을 완벽히 돌았다는 건 string의 전체 글자 수만큼 input_string을 탐색했을 때
            # 완전히 일치한다는 얘기기 때문에 print하고 현재 test case 탈출
            else:
                # string의 첫 번째 글자와 반복이 확인 된 input_string의 다음 글자를 비교해서 같으면 print
                if string[0] == input_string[i]:
                    print(f"#{t + 1} {len(string)}")
                    break
                # 아니면 글자 추가 후 다시 비교
                string = input_string[:i + 1]
        i += 1

