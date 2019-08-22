for T in range(1, int(input()) + 1):
    N = int(input())
    al = list(map(int, input().split()))
    max_n = al[0]
    min_n = al[0]
    for i in al:
        if i > max_n:
            max_n = i
        elif i < min_n:
            min_n = i
    print(f"#{T} {max_n-min_n}")

    