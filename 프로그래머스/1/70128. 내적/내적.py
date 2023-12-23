def solution(a, b):
    answer = 0
    for az, bz in zip(a,b):
        answer += az*bz
    return answer