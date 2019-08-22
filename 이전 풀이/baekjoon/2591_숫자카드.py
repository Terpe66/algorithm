import sys
sys.stdin = open("2591.txt")

def find(start = 0, end = 1, chk = True):
    global ans

    if end > length or chk == False:
        if chk:
            ans += 1
        return

    num = ""
    while start < length and start <= end:
        num += N[start]
        if int(num) <= 34:
            find(start + 1, start + 2)
        else:
            find(start + 1, start + 2, False)
        start += 1

N = input()
length = len(N)
ans = 0
find()

print(ans)