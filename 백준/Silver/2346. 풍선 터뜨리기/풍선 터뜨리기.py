from collections import deque

a = int(input())

list = input().split()
d = deque()

for idx, item in enumerate(list):
    d.append((idx, int(item)))

da, db = d.popleft()

answer = [str(da+1)]
current = db

while d:
    if current > 0 :
        for i in range(current):
            a, b = d.popleft()
            if i + 1 == current:
                answer.append(str(a + 1))
                current = b
            else:
                d.append((a, b))
    else:
        s = abs(current)
        for i in range(s):
            a,b = d.pop()
            if i + 1 == s:
                answer.append(str(a + 1))
                current = b
            else:
                d.appendleft((a, b))

print(' '.join(answer))