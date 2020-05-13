import sys
sys.stdin = open("4366.txt")

for t in range(int(input())):
    # money_2 : 2진수 숫자, money_3 : 3진수 숫자
    money_2 = input()
    money_3 = input()
    # int_money_2 : money_2를 10진수로 변환해서 값이 얼마인지 확인
    int_money_2 = int(money_2, 2)
    # i : 비트 연산을 하기 위한 index 값
    i = len(money_2) - 1
    # limit : money_3(3진수 숫자)의 길이가 얼마인지 확인하기 위한 변수
    limit = len(money_3)
    while i >= 0:
        # j : 3의 n승을 확인하기 위한 변수, k : 3의 j승의 n배수를 확인하기 위한 변수
        # 예시의 212는 3의 2승의 2배수, 3의 1승의 1배수, 3의 0승의 2배수
        j = k = 0
        # j는 3의 0승부터 보고, 길이를 넘어가면 안 되기 때문에
        while j < limit:
            # fake : 3진수 숫자를 10진수로 변환하고, 3의 j승을 빼서 3의 j승의 값을 0으로 만들어서 저장하는 변수
            # 예시의 212는 18 + 3 + 2 = 23이고, j가 0일 때 3 ** 0 * int(money_3[-1]) == 3 ** 0 * 2이기 때문에 18 + 3 + 0 = 21로 변경된다!
            fake = int(money_3, 3) - 3 ** j * int(money_3[- 1 - j])
            # ^ : xor 연산, ^ 왼쪽과 오른쪽이 모두 1이면 0 아니면 1, 스위치 켜고 끄기로 생각하면 됩니다
            # i가 가장 큰 값부터 줄어들기 때문에 예시에서 처음 연산은 1010(왼쪽)과 1000(오른쪽)을 연산해서 0010(2)로 만들어서 확인하는 식
            # 계산 상 2진수의 값만 변경하고 3진수의 j승의 값을 변경하지 않아도 같은 수가 될 수 있기 때문에 str(k)로 변했는지 아닌지 확인
            if int_money_2 ^ (1 << i) == fake + 3 ** j * k and money_3[- 1 - j] != str(k):
                print(f"#{t + 1} {int_money_2 ^ (1 << i)}")
                i = -1
                break
            else:
                # n배수 값인 k를 증가시킨다
                k += 1
                # 3진수는 2배수까지 밖에 없기 때문에 3이면 0으로 초기화 n승 값인 j를 증가
                if k == 3:
                    j += 1
                    k = 0
        i -= 1