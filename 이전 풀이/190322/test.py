arr = [1, 2, 3, 4, 5]
N = len(arr)
for i in range(1 << N):
    for j in range(N-1, -1, -1):
        if i & (1 << j) != 0:
            print(arr[N - 1 - j], end=" ")
    print()