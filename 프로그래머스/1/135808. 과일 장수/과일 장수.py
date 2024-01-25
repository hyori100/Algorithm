def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    alist = [i for i in score if i<=k]
    for i in range(0, len(alist), m):
        newList = alist[i:i+m]
        answer += (min(newList)*m if len(newList) == m else 0)
    return answer