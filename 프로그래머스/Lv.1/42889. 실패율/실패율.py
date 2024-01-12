def solution(N, stages):
    answer = []
    currentNum = len(stages)
    for stage in range(1, N+1):
        failSum = sum([1 for i in stages if i == stage])
        if currentNum == 0 :
            answer.append((stage, 0))
        else:
            answer.append((stage, failSum/currentNum))
        currentNum -= failSum
    answer = sorted(answer, key = lambda x:(-x[1], x[0]))
    return [a for a,b in answer]