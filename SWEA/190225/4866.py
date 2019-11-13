import sys
sys.stdin = open("4866.txt")

for t in range(int(input())):
    bracket = input()
    S = []
    result = 1
    for b in bracket:
        if b not in ("(", "{", "[", "]", "}", ")"):
            pass
        elif b == "(" or b == "{" or b == "[":
            S.append(b)
        elif b == ")":
            if not S or S.pop() != "(":
                result = 0
                break
        elif b == "}":
            if not S or S.pop() != "{":
                result = 0
                break
        elif b == "]":
            if not S or S.pop() != "[":
                result = 0
                break

    if S:
        result = 0

    print(f"#{t+1} {result}")
