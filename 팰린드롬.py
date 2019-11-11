def solution(s):
    answer = 0
    length = len(s)

    idx = 0
    leng = length - 1
    while idx < length and answer == 0:
        if s[idx] == s[leng + idx]:
            i, l = idx, leng
            while s[i] == s[l]:
                if i + 1 == l or i == l:
                    answer = leng - idx + 1
                    break
                i += 1
                l -= 1
        elif idx + leng == length - 1:
            leng -= 1
            idx = 0
        else:
            idx += 1

    return answer

solution("abcdcba")