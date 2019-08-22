import sys
sys.stdin = open("4873.txt")

for t in range(int(input())):
    string = input()

    idx = 0
    while idx+1 < len(string):
        if string[idx] == string[idx+1]:
            string = string[:idx] + string[idx+2:]
            if idx:
                idx -= 1
            else:
                idx = 0
        else:
            idx += 1

    print(f"#{t+1} {len(string)}")