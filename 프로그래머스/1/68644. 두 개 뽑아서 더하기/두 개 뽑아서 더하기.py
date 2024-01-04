from itertools import combinations

def solution(numbers):
    answer = set()
    combs = combinations(numbers, 2)
    for comb in combs:
        answer.add(sum(comb))
    return sorted(answer)