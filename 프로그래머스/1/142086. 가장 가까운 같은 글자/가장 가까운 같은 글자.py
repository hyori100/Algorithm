def solution(s):
    answer = []
    dic = {}
    for index, value in enumerate(s):
        if value in dic:
            intervalCnt = index - dic[value]
            answer.append(intervalCnt)
        else:
            answer.append(-1)
        dic[value] = index

    return answer