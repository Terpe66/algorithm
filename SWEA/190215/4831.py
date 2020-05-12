for T in range(1, int(input())+1):
    M, BS, C = map(int, input().split())
    cl = [0] * BS
    c = list(map(int, input().split()))
    
    for i in c:
        cl[i] = i
    c += [len(cl)]
    
    m = M
    cnt = 0
    for i in range(C):
        if i+1 < len(c) and c[i+1] - c[i] > m:
            M = 0
            break
    if M == 0:
        print(f"#{T} {cnt}")
    
    while M > 0:        
        for i in range(BS):
            if cl[i] == 0:
                m -= 1
            elif c[c.index(cl[i])+1] - i > m:
                m = M - 1
                cnt += 1
            else:
                m -= 1
        break
            
    if cnt:
        print(f"#{T} {cnt}")

