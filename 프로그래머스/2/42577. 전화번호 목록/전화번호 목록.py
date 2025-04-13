def solution(phone_book):
    d = {p:True for p in phone_book}
    
    for i in d:
        s = ""
        for number in i:
            s += number
            if s != i and s in d:
                return False
    return True