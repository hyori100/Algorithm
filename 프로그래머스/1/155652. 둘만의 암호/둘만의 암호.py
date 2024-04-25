def solution(s, skip, index):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    for i in skip:
        alpha = alpha.replace(i, '')
    for a in s:
        resultNum = (alpha.find(a) + index) % len(alpha)
        answer = answer + alpha[resultNum]
    return answer