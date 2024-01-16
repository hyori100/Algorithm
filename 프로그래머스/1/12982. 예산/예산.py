import itertools

def solution(d, budget):
    d.sort()
    hBudget = 0
    for index, value in enumerate(d):
        hBudget += value
        if hBudget > budget:
            return index
    return len(d)