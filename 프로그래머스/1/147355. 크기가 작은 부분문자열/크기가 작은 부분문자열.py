def solution(t, p):
    answer = 0
    nums = []
    pLen = len(p)
    listT = list(t)
    for index, value in enumerate(listT):
        if index + pLen < len(listT)+1 and int("".join(listT[index:index+pLen])) <= int(p):
            answer += 1
    return answer
            