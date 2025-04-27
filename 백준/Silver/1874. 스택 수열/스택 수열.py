import sys

N = int(sys.stdin.readline())
numList = [int(sys.stdin.readline()) for i in range(N)]

current = 0
stack= []
answer = []

for i in numList:
    while not stack or stack[-1] != i:
        if current == N:
            break
        current += 1
        stack.append(current)
        answer.append("+")
    if stack and stack[-1] == i:
        stack.pop()
        answer.append("-")

if stack:
    print("NO")
else:
    for i in answer:
        print(i)