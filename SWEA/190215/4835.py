for T in range(1, int(input())+1):
    A, N = map(int, input().split())
    num_list = list(map(int, input().split()))
    min_sum = num_list[0]
    
    for i in range(1, N):
        min_sum += num_list[i]
    
    max_sum = min_sum
    
    for i in range(len(num_list)-N+1):
        sum_num = 0
        cnt = 0
        while cnt < N:
            sum_num += num_list[i+cnt]
            cnt += 1
        
        if sum_num < min_sum:
            min_sum = sum_num
        elif sum_num > max_sum:
            max_sum = sum_num
            
    print(f"#{T} {max_sum - min_sum}")


