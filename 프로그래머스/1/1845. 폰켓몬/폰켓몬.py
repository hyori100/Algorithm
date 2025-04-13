import collections
def solution(nums):
    d = collections.Counter(nums)

    if len(nums)/2 < len(d):
        return len(nums)/2
    else:
        return len(d)
