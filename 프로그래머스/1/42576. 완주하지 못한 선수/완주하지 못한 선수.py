import collections

def solution(participant, completion):
    cdic = collections.Counter(completion)
    
    for p in participant:
        if p in cdic and cdic[p] > 0:
            cdic[p] = cdic[p] - 1
        else:
            return p