def solution(t, p):
    answer = 0
    listT = list(t)
    for index, value in enumerate(listT):
        if index + len(p) < len(listT)+1 and int("".join(listT[index:index+len(p)])) <= int(p):
            answer += 1
    return answer
            