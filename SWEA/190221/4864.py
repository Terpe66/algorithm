for T in range(int(input())):
    str1 = input()
    str2 = input()
    
    idx = 0
    while idx < len(str1):
        for i in range(len(str2)):
            if idx == len(str1):
                break
            if str1[idx] != str2[i]:
                idx = 0
            else:
                idx += 1
        else:
            break
    
    if idx == len(str1):
        print("#{} 1".format(T+1))
    else:
        print("#{} 0".format(T+1))