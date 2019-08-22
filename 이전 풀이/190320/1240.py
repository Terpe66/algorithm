import sys
sys.stdin = open("1240.txt")

pw = ("0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011")

for t in range(int(input())):
    height, width = map(int, input().split())
    board = []

    for _ in range(height):
        board.append(input())

    password = ""
    i = width
    for B in board:
        if B == "0" * width:
            continue
        while i - 7 >= 0:
            for idx in range(10):
                if pw[idx] == B[i - 7:i]:
                    password = str(idx) + password
                    i -= 7
                    break
            else:
                i -= 1
        break

    odd = even = 0
    for i in range(7):
        if i % 2:
            even += int(password[i])
        else:
            odd += int(password[i])

    print(f"#{t + 1}", end=" ")
    if (odd * 3 + even + int(password[-1])) % 10 == 0:
        print(odd + even + int(password[-1]))
    else:
        print(0)