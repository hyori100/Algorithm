from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split()) # 10 3
seqList = list(map(int, sys.stdin.readline().split())) #2 9 5

d = deque([i+1 for i in range(N)]) # 1 2 3 4 5 6 7 8 9 10
cnt = 0

for i in range(M):
    #왼쪽에 남은 개수보다 오른쪽에 남은 개수가 클 때 => popleft()
    #오른쪽에 남은 개수보다 왼쪽에 남은 개수가 클 때 => pop() 
    #뽑으려는 숫자가 첫번째 원소로 올 때까지
    num = seqList[i]
    dIdx = d.index(num) + 1
    leftLen = dIdx - 1
    rightLen = len(d) - dIdx

    while d and d[0] != num:
        if leftLen <= rightLen:
            d.append(d.popleft())
        else:
            d.appendleft(d.pop())
        cnt += 1
    
    d.popleft()

print(cnt)
    