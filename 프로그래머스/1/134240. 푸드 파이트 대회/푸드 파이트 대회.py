def solution(food):
    answer = ''
    for index, value in enumerate(food[1:]):
        if value//2 > 0:
            answer += str(index + 1) * (value//2)
    answer += '0' + answer[::-1]
    return answer