def solution(arr1, arr2):
    answer = []
    rowLen = len(arr1)
    for i in range(0, rowLen):
        answer.append([x+y for x,y in zip(arr1[i], arr2[i])])
    return answer