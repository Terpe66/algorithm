import sys
sys.stdin = open("1946.txt")

for t in range(int(input())):
    # 현재 케이스 번호 출력
    print(f"#{t + 1}")
    ans = ""
    # 몇 번 입력 받을지는 range 안에 input 받음
    for _ in range(int(input())):
        # char : 글자(A), n : 압축된 수
        char, n = input().split()
        # ans에 char * int(n)을 더한다! (AAAAAAAAAA)
        ans += char * int(n)
    # 다 더한 뒤에는 10글자씩 출력한다
    i, idx = 0, len(ans)
    while i < idx:
        print(ans[i:i+10])
        i += 10