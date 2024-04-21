def solution(X, Y):
    dicY = dict()
    numList = []
    for i in Y:
        if i in dicY:
            dicY[i] = dicY[i] + 1
        else:
            dicY[i] = 1
    
    for item in X:
        if item in dicY and dicY[item] != 0:
            dicY[item] = dicY[item] - 1
            numList.append(item)
    if not numList:
        return "-1"
    elif numList.count("0") is len(numList):
        return "0"
    else:
        numList.sort(reverse=True)
        return ''.join(numList)