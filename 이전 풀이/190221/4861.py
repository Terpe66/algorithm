import sys
sys.stdin = open("4861.txt", "r")

for T in range(int(input())):
    line, length = map(int, input().split())
    charlist = []
    for char in range(line):
        charlist.append(input())
    cnt = 0
    result = ""
    for i in range(line):
        j = 0
        if result != "":
            break
        while j + length - 1 - cnt < line:
            if cnt >= length:
                result = charlist[i][j-cnt//2:j+cnt//2+1]
                break
            if cnt == 0 and charlist[i][j] != charlist[i][j + length - 1 - cnt]:
                j += 1
            elif charlist[i][j] != charlist[i][j + length - 1 - cnt]:
                cnt = 0
            else:
                cnt += 2
                j += 1
    
    if result == "":
        for i in range(line):
            j = 0
            if result != [""] * length:
                break
            while j + length - 1 - cnt < line:
                if cnt >= length:
                    idx = j + length - 1 - cnt
                    for c in range(j - cnt//2, j + cnt//2 + 1)
                        result += charlist[c][i]
                if cnt == 0 and charlist[j][i] != charlist[j + length - 1 - cnt][i]:
                    j += 1
                elif charlist[j][i] != charlist[j + length - 1 - cnt][i]:
                    cnt = 0
                else:
                    cnt += 2
                    j += 1
    print("#{} {}".format(T+1, "".join(result)))