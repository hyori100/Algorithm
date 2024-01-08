from itertools import combinations

def is_prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    for i in combinations(nums, 3):
        if is_prime_num(sum(i)) == True:
            answer += 1
    return answer