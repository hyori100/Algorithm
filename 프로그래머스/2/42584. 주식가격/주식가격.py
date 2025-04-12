from collections import deque

def solution(prices):
    q = deque()
    answer = []
    for idx, p in enumerate(prices):
        q.append((idx, p))
    while q:
        idx, item = q.popleft()
        for a,b in q:
            index = a
            if item > b:
                break
        answer.append(index-idx)
    return answer