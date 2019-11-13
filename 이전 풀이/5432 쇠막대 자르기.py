import sys
sys.stdin = open("5432.txt")

for t in range(int(input())):

    inputs = input()
    length = len(inputs)
    i = 0
    stick = 0
    ans = 0
    while i < length:
        if i + 1 < length and inputs[i] == "(" and inputs[i + 1] == ")":
            ans += stick

        elif i + 1 < length and inputs[i] == inputs[i + 1] == "(":
            stick += 1
            ans += 1

        elif i + 1 < length and inputs[i] == inputs[i - 1] == ")":
            stick -= 1

        i += 1

    print("#{} {}".format(t + 1, ans))