def solution(n):
    c = list(map(int, list(str(n)))) # c=list(str(n)) - int로 변환하지않아도 sort 가능
    c.sort(reverse=True)
    return int(''.join(list(map(str, c)))) #int(''.join(c)) 