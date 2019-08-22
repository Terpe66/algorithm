import sys
sys.stdin = open("5356.txt")

for t in range(int(input())):
    string = []
    length = 0
    for _ in range(5):
        inputs = input()
        if len(inputs) > length:
            length = len(inputs)
        string.append(inputs)

    print(f"#{t+1}", end=" ")
    for row in range(length):
        for col in range(5):
            if len(string[col]) > row:
                print(string[col][row], end="")
    print()
