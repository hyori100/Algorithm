import math
def solution(progresses, speeds):
    works = []
    stack = []
    answer = []
    for idx, progress in enumerate(progresses):
        work = math.ceil((100 - progress) / speeds[idx])
        works.append(work)
    front = 0

    for idx in range(len(works)):
        if works[idx] > works[front]:  
            answer.append(idx - front)
            front = idx 
    answer.append(len(works) - front) 
    return answer