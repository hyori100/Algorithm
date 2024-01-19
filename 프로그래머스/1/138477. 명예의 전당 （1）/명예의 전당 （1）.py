def solution(k, score):
    answer = []
    mvps = []
    for item in score:
        if len(mvps) < k:
            mvps.append(item)
        elif mvps[k-1] < item:
            mvps[k-1] = item
        answer.append(min(mvps))
        mvps.sort(reverse=True)#정렬하면 시간 오래 걸릴 것을 감안..
    return answer