num = list(map(int, input().split()))

max_n = 0
for n in num:
    if n > max_n:
        max_n = n
num.remove(max_n)

if num[0] >= num[1]:
    print(num[0])
else:
    print(num[1])