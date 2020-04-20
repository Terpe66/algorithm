def solution(genres, plays):
    answer = []
    ans_dict = {}
    for idx in range(len(genres)):
        if genres[idx] not in ans_dict:
            ans_dict[genres[idx]] = [(plays[idx], idx)]
        else:
            ans_dict[genres[idx]].append((plays[idx], idx))

    for key in ans_dict.keys():
        ans_dict[key] = sorted(ans_dict[key], reverse=True)

    rank = []
    for key in ans_dict.keys():
        rank.append((plays[ans_dict[key][0][1]], key))
    rank = sorted(rank, reverse=True)

    for r in rank:
        length = len(ans_dict[r[1]])
        if length == 2:
            answer.append(ans_dict[r[1]][0][1])
            answer.append(ans_dict[r[1]][1][1])
        elif length > 2:
            i = 0
            tmp = None
            cnt = 0
            while i < length - 1:
                if ans_dict[r[1]][i][0] == ans_dict[r[1]][i + 1][0]:
                    tmp = i
                else:
                    answer.append(ans_dict[r[1]][i][1])
                    cnt += 1
                    if cnt == 2:
                        break

                if tmp and ans_dict[r[1]][i][0] != ans_dict[r[1]][i + 1][0]:
                    answer.append(ans_dict[r[1]][i][1])
                    cnt += 1
                if cnt == 2:
                    break
                i += 1
                if tmp and i + 1 == length:
                    answer.append(ans_dict[r[1]][-1][1])
        else:
            answer.append(ans_dict[r[1]][0][1])

    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 500, 800, 2500])