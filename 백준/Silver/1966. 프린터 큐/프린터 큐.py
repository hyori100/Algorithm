import sys
from collections import deque

N = int(sys.stdin.readline())

def sqare(x):
    return x[1]

def checkSequence(numbers, seq):
    cnt = 0 
    while numbers:
        if max(list(map(sqare, numbers))) > numbers[0][1]:
            idx, num = numbers.popleft()
            numbers.append((idx, num))
        else:
            idx, num = numbers.popleft()
            cnt += 1
            if idx == seq:
                print(cnt)
                break

for i in range(0,N):
    _, targetSeq = map(int, sys.stdin.readline().split())
    d = deque()
    for idx, item in enumerate(list(map(int, sys.stdin.readline().split()))):
        d.append((idx, item))
    checkSequence(d, targetSeq)