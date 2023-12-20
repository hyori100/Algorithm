def solution(a, b):
    answer = []
    if a == b :
        return a
    elif a<b:
        s = range(a,b+1)
    else:
        s = range(a,b-1,-1)

    for i in s:
        answer.append(i)
    return sum(answer)