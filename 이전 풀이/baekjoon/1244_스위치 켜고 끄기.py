import sys
sys.stdin = open("1244.txt")

N = int(input())
switch = list(map(int, input().split()))
S = int(input())
student = []
for _ in range(S):
    student.append(tuple(map(int, input().split())))

for i in student:
    idx = 0
    if i[0] == 1:
        idx = i[1]-1
        while idx < N:
            if switch[idx]:
                switch[idx] = 0
            else:
                switch[idx] = 1
            idx += i[1]
    else:
        cnt = 1
        idx = i[1]-1
        if switch[idx]:
            switch[idx] = 0
        else:
            switch[idx] = 1

        while idx - cnt >= 0 and idx + cnt < N:
            if switch[idx-cnt] == switch[idx+cnt]:
                if switch[idx-cnt]:
                    switch[idx-cnt], switch[idx+cnt] = 0, 0
                else:
                    switch[idx-cnt], switch[idx+cnt] = 1, 1
            else:
                break
            cnt += 1
cnt = 1
for i in range(N):
    if i == (20 * cnt):
        print()
        cnt += 1
    print(switch[i], end=" ")