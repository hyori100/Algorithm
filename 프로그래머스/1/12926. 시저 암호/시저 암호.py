def solution(s, n):
    answer = ''
    for i in list(s):
        if i == " ":
            answer += ' '
        elif i.islower():
            answer += chr(ord("a") + ((ord(i) + n - ord("a")) % 26))
        else:
            answer += chr(ord("A") + ((ord(i) + n - ord("A")) % 26))
    return answer