def solution(n, computers):
    answer = 0
    chk = [False] * n
    chk[0] = 1
    for idx, computer in enumerate(computers):
        i = 0
        if idx == 0:
            while i < len(computer):
                if computer[i] == 1:
                    chk[i] = chk[idx]
                i += 1
            continue

        while i < len(computer):
            if i != idx and computer[i] == 1:
                if chk[i] == False and chk[idx] != False:
                    chk[i] = chk[idx]

            i += 1

    print(chk)

    return answer

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])