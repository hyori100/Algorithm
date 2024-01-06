def solution(name, yearning, photo):
    answer = []
    dic = {}
    for name, yearning in zip(name, yearning):
        dic[name] = yearning
    for pho in photo:
        score = 0
        for s in pho:
            if s in dic:
                score += dic[s]
        answer.append(score)
    return answer