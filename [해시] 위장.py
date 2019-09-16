def solution(clothes):
    ans_dict = {}
    ans = 0

    for cloth in clothes:
        if cloth[1] not in ans_dict:
            ans_dict[cloth[1]] = [cloth[0]]
        else:
            ans_dict[cloth[1]].append(cloth[0])




    return ans


solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])