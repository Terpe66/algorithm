import sys
sys.stdin = open("1242.txt")

# 암호의 길이가 달라질 수 있기 때문에 "0"과 "1"의 비율을 저장
password = ((3, 2, 1, 1), (2, 2, 2, 1), (2, 1, 2, 2), (1, 4, 1, 1), (1, 1, 3, 2), (1, 2, 3, 1), (1, 1, 1, 4), (1, 3, 1, 2), (1, 2, 1, 3), (3, 1, 1, 2))
for t in range(int(input())):
    height, width = map(int, input().split())
    board = []
    for _ in range(height):
        # input의 가장 오른쪽의 "0"을 제거하고 append
        board.append(input().rstrip("0"))

    # used : 사용했던 암호를 담는 리스트, last : 가장 최근에 암호를 풀어낸 줄(row)을 건너 뛰기 위한 변수, ans : 답
    used = []
    last = ""
    ans = 0
    # board의 row를 하나씩 읽어온다.
    for pw in board:
        # input을 append할 때 rstrip("0")을 하면 전체가 "0"인 줄은 모두 삭제되기 때문에 pw == ""
        # "0"이 아닐 때, 가장 최근에 풀어낸 줄과 같은 줄이면 통과
        if pw == "" or pw == last:
            continue
        # 처음 읽는 암호가 있는 줄을 last에 저장해서 다음 번에 같은 줄이 들어오면 continue
        last = pw
        # 사용한 암호가 있는 지 확인하고 삭제하는 for문
        for key in used:
            # 현재 읽는 줄에 사용한 암호가 있으면
            if key in pw:
                # i : 사용한 암호가 시작되는 index를 찾아 저장하는 변수
                i = pw.index(key)
                # 현재 읽는 줄의 시작부터, 사용한 암호가 시작되는 index 직전까지를 저장
                    # rstrip("0")으로 사용한 암호 왼쪽의 "0"을 제거("00000[암호]00000[사용한암호]0000..."라면 사용한 암호 왼쪽의 "0"은 불필요하기 때문에)
                # 사용한 암호가 시작되는 index부터 그 암호의 길이만큼을 제외("00000[암호]0000...[암호]..."의 모양으로 만듦)
                pw = pw[:i].rstrip("0") + pw[i + len(key):]
        # 암호 코드(2진수)의 형태가 0101의 형태기 때문에 가장 오른쪽부터 읽어야 한다
        # 암호 코드의 길이를 모르고, 길이가 길어질 경우에 왼쪽의 "0"이 얼마나 필요한지 모르기 때문에
            # (0011001이 길어지면 00001111000011이 되고, 더 길어지면 000000111111000000111이 돼서)
        for i in range(len(pw) - 1, -1, -1):
            # PW : 암호를 암호 코드(2진수)로 변환한 값을 해석해서 저장하는 변수
            # num : used에 넣을 암호를 저장하는 변수
            # insert : 암호를 암호 코드로 변환해 저장하는 변수
            PW = num = insert = ""
            # multi : 암호 코드의 길이를 모르기 때문에 비율을 늘려주기 위한 변수
            multi = 1
            while i >= 0:
                # go : 암호를 암호 코드로 변환해 저장하는 변수, insert는 go를 모두 더한 변수
                go = ""
                # insert가 비어있고, 현재 읽는 줄의 i번째 index가 "0"이면 해석할 필요가 없기 때문에 i를 -1해주고 continue
                if insert == "" and pw[i] == "0":
                    i -= 1
                    continue
                # continue 되지 않으면 해석해야 하기 때문에 암호(pw[i]를 num에 저장)
                num += pw[i]
                # 현재 읽고 있는 16진수 암호 한 글자를 10진수로 변경하고 bit연산으로 2진수로 변경
                for j in range(3, -1, -1):
                    if int(pw[i], 16) & (1 << j):
                        go += "1"
                    else:
                        go += "0"
                # 오른쪽부터 읽기 때문에 새로운 부분을 계속 왼쪽에 더해줌
                insert = go + insert
                # 가장 오른쪽의 0은 읽을 필요가 없기 때문에 rstrip("0")
                if insert[-1] == "0":
                    insert = insert.rstrip("0")

                # insert의 길이가 7(암호 코드의 기본 길이) * multi(혹시 길어질 수 있기 때문에)
                if len(insert) >= 7 * multi:
                    # 암호를 오른쪽부터 읽기 때문에 변환도 insert의 가장 오른쪽부터 해준다!
                    j = len(insert)
                    # 암호 코드는 0~9까지기 때문에 range(10)
                    for idx in range(10):
                        # word : 암호 코드 튜플에서 코드에 길이(multi)를 곱해서 저장하는 변수
                        word = password[idx][0] * "0" * multi + password[idx][1] * "1" * multi + password[idx][2] * "0" * multi + password[idx][3] * "1" * multi
                        # insert의 제일 뒤부터 7번째까지의 숫자가 현재의 word(암호 코드)와 같으면
                        if insert[j - (7 * multi):j] == word:
                            # 암호를 해석한 값(암호 코드 튜플의 index)을 PW에 저장
                            PW += str(idx)
                            # 방금 해석한 부분을 insert에서 제외
                            insert = insert[:j - (7 * multi)]
                            # 해석한 값이 8이 되면 올바른 암호인지 확인해야 하기 때문에
                            if len(PW) == 8:
                                # used에 현재까지 저장한 num을 뒤집어서 저장(역순으로 봤기 때문에)
                                used.append(num[::-1])
                                # even, odd : 홀수번째 짝수번째를 구분하기 위한 변수
                                even = odd = 0
                                # num은 뒤집어서 저장했지만 PW는 아직 뒤집어진 상태기 때문에 가장 오른쪽이 아니라 가장 왼쪽이 검사 코드가 된다
                                for k in range(1, 8):
                                    if k % 2:
                                        even += int(PW[k])
                                    else:
                                        odd += int(PW[k])
                                # 검사를 통과할 경우 정답으로 저장
                                if (even * 3 + odd + int(PW[0])) % 10 == 0:
                                    ans += even + odd + int(PW[0])
                                # 통과했든 아니든 사용했던 num, insert, PW, multi를 초기화
                                num = insert = PW = ""
                                multi = 1
                                # pw를 현재까지 읽은 암호의 이전 index까지로 설정하고 rstrip("0")
                                pw = pw[:i].rstrip("0")
                                # rstrip("0")으로 길이가 줄었을 수 있기 때문에 i의 값도 pw의 가장 오른쪽으로 변경(안 해주면 index 에러)
                                i = len(pw)
                            break
                    # for else로 for문으로 10개의 암호 코드를 확인했을 때 저장되는 값이 없다면(break 되지 않았다면)
                    # 길이가 길다는 얘기이기 때문에 multi를 +1 해서 코드를 길게 확인
                    else:
                        multi += 1
                # i를 계속 줄여가면서 왼쪽으로 확인
                i -= 1
            break

    print(f"#{t + 1} {ans}")