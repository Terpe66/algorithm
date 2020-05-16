import sys
sys.stdin = open("13458.txt")

for T in range(int(input())):
    answer = 0

    room = int(input())
    students = list(map(int, input().split()))
    mainT, subT = map(int, input().split())

    for i in range(room):
        students[i] -= mainT
        answer += 1
        if students[i] > 0:
            sub = students[i] // subT
            if students[i] % subT:
                sub += 1
            answer += sub

    print(answer)