def solution(s):
    pCount=0
    sCount=0
    
    for i in s:
        if i=="p" or i=="P":
            pCount += 1
        elif i=="y" or i=="Y":
            sCount += 1
            
    if pCount == sCount:
        return True
    else:
        return False