from collections import deque

a = int(input())

list = input().split()
d = deque([int(i) for i in list])

current = 1
stack = []

while d:
    i = d.popleft()
    if current == i:
        current += 1
    else:
        while stack and stack[-1] == current:
            v = stack.pop()
            current += 1
        stack.append(i)

while stack:
    v = stack.pop()
    if v == current:
        current += 1
    else:
        break

if stack:
    print("Sad")
else:
    print("Nice")

