def solution(clothes):
    dict = {}
    
    for cloth in clothes:
        if cloth[1] not in dict:
            dict[cloth[1]] = 1
        else:
            dict[cloth[1]] += 1
    
    answer = 1
    for a,b in dict.items():
        answer *= (b+1)
    return answer - 1
        