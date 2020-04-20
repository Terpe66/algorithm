import sys
sys.stdin = open("1244.txt")

for t in range(int(input())):
    M, C = map(str, input().split())
    c = C = int(C)
    M = list(map(str, M))
    length = len(M)
    Is = []
    i = 0

    for i in range(length - 1):
        if c == 0:
            break
        # if c: # if c > 0:
        comp = (i, M[i])
        chk = True
        for j in range(i + 1, length):
            if comp[1] < M[j]:
                comp = (j, M[j])
                chk = False
        if chk == False:
            M[i], M[comp[0]] = comp[1], M[i]
            Is.append((i, comp[0]))
            c -= 1

    while i < length - 2 and c:
        j = length - 1
        comp = (i, M[i])
        chk = True
        while i < j:
            if comp[1] < M[j]:
                comp = (j, M[j])
                chk = False
            j -= 1
        if chk == False:
            M[i], M[comp[0]] = comp[1], M[i]
            Is.append((i, comp[0]))
            c -= 1
        i += 1

    if c % 2:
        for i in range(length - 1):
            if M[i] == M[i + 1]:
                break
        else:
            M[length - 2], M[length - 1] = M[length - 1], M[length - 2]
            c = 0

    for i in range(len(Is) - 1):
        if M[Is[i][0]] == M[Is[i + 1][0]] and M[Is[i][1]] > M[Is[i + 1][1]]:
            M[Is[i][1]], M[Is[i + 1][1]] = M[Is[i + 1][1]], M[Is[i][1]]

    print(f"#{t + 1} {''.join(M)}")