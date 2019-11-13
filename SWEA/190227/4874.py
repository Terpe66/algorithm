import sys
sys.stdin = open("4874.txt")

for t in range(int(input())):
    F = input().split()
    asmd = ("+", "-", "*", "/")
    S = []
    ans = ""
    if len(F) < 4:
        print(f"#{t+1} error")
        continue
    for f in F:
        if f == ".":
            if len(S) == 1:
                ans = S.pop()
            else:
                ans = "error"
                break
        elif f in asmd:
            if len(S) < 2:
                ans = "error"
                break          
            b = S.pop()
            a = S.pop()
            if f == "+":
                S.append(a + b)
            elif f == "-":
                S.append(a - b)
            elif f == "*":
                S.append(a * b)
            elif f == "/":
                S.append(a // b)
        else:
            S.append(int(f))
            
    print(f"#{t+1} {ans}")