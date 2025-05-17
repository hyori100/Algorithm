import sys

N, M = map(int, input().split())
numstr = map(int, sys.stdin.readline().strip())
stack = []

cnt = 0
for num in numstr:
    while cnt < M and stack and stack[-1] < num:
        stack.pop()
        cnt += 1
    stack.append(num)

print(''.join(map(str,stack[:N-M])))