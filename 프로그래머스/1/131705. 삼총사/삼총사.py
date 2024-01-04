from itertools import combinations

def solution(numbers):
    answer = 0
    combs = list(combinations(numbers,3))
    for comb in combs:
        if sum(comb) == 0:
            answer += 1
    return answer