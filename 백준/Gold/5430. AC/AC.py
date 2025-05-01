import sys
from collections import deque
        
N = int(sys.stdin.readline().strip())

for i in range(N):
    cal = sys.stdin.readline().strip().replace("RR","")
    listlen = int(sys.stdin.readline().strip())
    numList = sys.stdin.readline().strip()

    if numList != "[]":
        numList = deque(numList[1:-1].split(',')) #[, ], 쉼표 제거
    else:
        numList = deque()

    isError = False
    direction = 1

    if cal.count("D") > len(numList):
        print("error")
        continue
    
    for i in cal:
        if i == "R":
            direction *= -1
        elif i == "D":
            if not numList:
                isError = True
                break
            if direction == True:
                numList.popleft()
            else:
                numList.pop()
    if direction == -1:
        numList.reverse()
    print("error" if isError else '['+','.join(map(str, numList))+']')
