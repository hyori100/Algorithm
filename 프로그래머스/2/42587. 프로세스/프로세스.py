from collections import deque

def solution(priorities, location):
    q = deque()
    sequence = 0
    for idx, p in enumerate(priorities):
        q.append((idx, p))
    while q:
        maxNum = max([b for a,b in q])
        idx, item = q.popleft()
        if item < maxNum:
            q.append((idx,item))
        else:
            sequence += 1
            if idx == location:
                return sequence
