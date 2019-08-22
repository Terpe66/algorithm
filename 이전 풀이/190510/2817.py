import sys
sys.stdin = open("2817.txt")

#6) 함수를 정의해줍니다. 함수의 진행 방식은
#6-1) numbers의 0번 index부터 더한 뒤에 1, 2, ..., N번 index까지 탐색합니다.
#6-2) 탐색하는 index의 방문 여부를 체크하고,
#6-3) 현재까지 더한 값인 num과 지금 탐색 중인 numbers[index]의 값을 더했을 때 목표값 K를 넘지 않는지 체크합니다.
#6-4) 6-3까지 조건을 통과했을 때 다시 함수로 진입합니다.
#6-5) 중복을 제외하기 위해서 현재 index의 이전 index는 탐색하지 않아요
#예) 0번 index부터 탐색해서 0 + 1 + 2의 결과를 얻었는데, 2번 index부터 탐색할 때 2 + 0 + 1을 보는 걸 제외
#6-6) 모든 index를 탐색한 후에 현재까지 더한 값인 num이 목표값 K와 같다면 ans를 1 추가합니다.

#6-7) idx: 함수에 들어가면서 탐색을 시작할 index, num: 탐색하면서 조건을 충족하면 더하는 값(K가 될 값)
def sumnum(idx, num):

    #7) ans가 함수 진행 중에 변경되기 때문에 global로 선언해요
    global ans

    #8) [6-5] 현재 탐색 중인 index 이전 index는 보지 않기 위해 range(idx, N)으로 설정해줍니다.
    for i in range(idx, N):

        #9) [6-2] for문에서 탐색 중인 index에 방문했는지 체크하고, [6-3] num과 numbers[index]의 합이 K를 넘는지 체크해요
        if visit[i] == False and num + numbers[i] <= K:

            #10) 조건을 충족하면 더해야 하는 값이기 때문에 "함수에 들어가기 전"에 방문 체크를 해줍니다
            visit[i] = True

            #11) [6-4] 함수에 다시 진입해요(0번 index부터 더하고, 현재 탐색 중인 index인 i, num과 numbers[index] 값을 넘겨주면서)
            sumnum(i, num + numbers[i])

            #12) 함수가 끝나고 나오면 방문 체크를 다시 풀어줍니다
            visit[i] = False

    #13) 마지막 index까지 탐색하고 나왔을 때의 num이 K와 같다면 ans를 +1 해줍니다
    if num == K:
        ans += 1
        return


for T in range(int(input())):
    #1) 숫자 개수 N, 더해야 하는 값 K를 input 받습니다.
    N, K = map(int, input().split())

    #2) 숫자 집합(numbers)을 input 받습니다.
    numbers = list(map(int, input().split()))

    #3) 같은 index의 숫자를 더하는 것을 방지하기 위해서 방문 체크 리스트를 만듭니다.
    visit = [False for _ in range(N)]

    #4) ans는 몇 개가 더해지는지 체크하는 변수입니다.
    ans = 0

    #5) 함수를 실행하는 구간입니다.
    sumnum(0, 0)

    print(f"#{T + 1} {ans}")