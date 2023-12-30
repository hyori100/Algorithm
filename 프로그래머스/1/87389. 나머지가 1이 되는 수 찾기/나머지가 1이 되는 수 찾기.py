def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n//i * i == n-1:
            answer = i
            break;
    return answer