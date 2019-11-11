def solution(priorities, location):
    answer = 0
    w = priorities[location]
    length = len(priorities)

    i = 0
    while True:
        if i == length:
            i = 0

        if priorities[i] == max(priorities):
            answer += 1
            priorities[i] = -1
            if i == location:
                break
        i += 1

    return answer

solution([1, 1, 9, 1, 1, 1], 0)