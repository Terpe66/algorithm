import sys
sys.stdin = open("3750.txt")

# 테스트 케이스가 10만 개라서 리스트에 모아뒀다가 for문으로 프린트
print_list = []
for _ in range(int(input())):
    num = input()
    # 입력 받은 숫자의 길이가 1보다 크면 반복문 진행(1이 될 경우 탈출)
    while len(num) > 1:
        # sub_num : 모든 자리수를 더하는 변수
        sub_num = 0
        # 입력 받은 숫자에서 한 개씩 꺼내는 반복문
        for n in num:
            # 꺼낸 숫자를 sub_num에 더하기
            sub_num += int(n)
        # int로 더한 값을 str으로 변경해서 num 변수에 넣어줌
        num = str(sub_num)
    # 출력을 위한 리스트에 num 값 추가
    print_list.append(num)

for i in range(len(print_list)):
    print(f"#{i + 1} {print_list[i]}")
