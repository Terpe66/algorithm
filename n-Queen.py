def find(idx=0):
    global ans, length

    if idx == length:
        ans += 1

    for i in range(length):
        if not row[i] and not col[idx]:
            chk = True
            rr, cc = idx, i
            # 좌우
            if row[cc]:
                chk = False

            # 상하
            if chk and col[rr]:
                chk = False

            if chk:
                rr, cc = idx, i
                # 우하
                while chk and 0 <= rr < length and 0 <= cc < length:
                    if row[cc] and col[rr]:
                        chk = False
                        break
                    rr += 1
                    cc += 1

            if chk:
                rr, cc = idx, i
                # 우상
                while chk and 0 <= rr < length and 0 <= cc < length:
                    if row[cc] and col[rr]:
                        chk = False
                        break
                    rr -= 1
                    cc += 1

            if chk:
                rr, cc = idx, i
                # 좌상
                while chk and 0 <= rr < length and 0 <= cc < length:
                    if row[cc] and col[rr]:
                        chk = False
                        break
                    rr -= 1
                    cc -= 1

            if chk:
                rr, cc = idx, i
                # 좌하
                while chk and 0 <= rr < length and 0 <= cc < length:
                    if row[cc] and col[rr]:
                        chk = False
                        break
                    rr += 1
                    cc -= 1

            if chk:
                row[i] = True
                col[idx] = True
                find(idx + 1)


def solution(n):
    global ans, length, row, col

    answer = 0

    length = n
    row = [False] * length
    col = [False] * length

    find()
    answer = ans
    ans = 0

    return answer


ans = 0
length = 0
row = []
col = []

solution(4)