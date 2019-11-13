import sys
sys.stdin = open("workshop.txt")

for t in range(10):
    length = int(input())
    nums = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    S = []
    N = []
    cal = input()
    
    for char in cal:
        if char in nums:
            N.append(char)
        elif char == ")":
            while S[-1] != "(":
                N.append(S.pop())
            S.pop()
        elif char == "*":
            if S[-1] == "*":
                N.append(S.pop())
                S.append(char)
            else:
                S.append(char)
        elif char == "+":
            if S[-1] == "*":
                N.append(S.pop())
                S.append(char)
            else:
                S.append(char)
        else:
            S.append(char)

    for f in N:
        if f in ("+", "*"):
            b = S.pop()
            a = S.pop()
            if f == "+":
                S.append(a + b)
            elif f == "*":
                S.append(a * b)
        else:
            S.append(f)

    print(f"#{t+1} {S.pop()}")




# (9+(5*2+1)+(3*3*7*6*9*1*7+1+8*6+6*1*1*5*2)*4*7+4*3*8*2*6+(7*8*4*5)+3+7+(2+6+5+1+7+6+7*3*(6+2)+6+6)*2+4+2*2+4*9*3)