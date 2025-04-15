def solution(genres, plays):
    answer = []
    dict = {}
    sumDict = {}
    for idx, item in enumerate(genres):
        if item not in dict:
            dict[item] = [(idx, plays[idx])]
        else:
            dict[item].append((idx, plays[idx]))
    for d in dict:
        dict[d].sort(key=lambda x: (-x[1], x[0]))
        sumDict[d] = sum(b for a,b in dict[d])
    sorted_dict = sorted(sumDict.items(), key= lambda item: -item[1])
    for a,b in sorted_dict:
        answer.append(dict[a][0][0])
        if len(dict[a]) > 1:   
            answer.append(dict[a][1][0])
    return answer
        