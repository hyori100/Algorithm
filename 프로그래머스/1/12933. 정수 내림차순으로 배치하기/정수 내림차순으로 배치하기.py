def solution(n):
    c = list(map(int, list(str(n))))
    c.sort(reverse=True)
    return int(''.join(list(map(str, c))))