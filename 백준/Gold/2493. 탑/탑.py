import sys
        
N = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))
stack = []

for i in range(N):
    cur = 0
    while stack:
        a,b = stack[-1]
        if b >= list[i]:
            cur = a + 1
            break
        stack.pop()
    stack.append((i, list[i]))
    print(cur)