for T in range(1, int(input())+1):
    N = int(input())
    C = list(map(int, input()))
    cnt_list = [0] * 10
    
    for i in C:
        cnt_list[i] += 1
    
    card = 0
    cnt = 0
    for idx in range(9, -1, -1):
        if cnt_list[idx] > cnt:
            cnt = cnt_list[idx]
            card = idx
    
    print(f"#{T} {card} {cnt}")



for test_case in (1, int(input())+1):
    N = int(input())
    cards = input()
    cnt = [0] * 10

    for ch in cards:
        val = int(ch)
        cnt[val] += 1
    Max = 0
    for i in range(1, len(cnt)):
        if cnt[Max] < cnt[i]:
            Max = i

    print(Max, cnt[Max])

    