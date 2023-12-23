def solution(s):
    if len(s) % 2 == 0:
        index = len(s)//2
        return s[index-1:index+1]
    else:
        return s[len(s)//2]