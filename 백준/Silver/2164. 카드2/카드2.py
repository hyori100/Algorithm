from collections import deque

n = int(input())
d = deque()

for i in range(1, n+1):
    d.append(i)

last = d[0]
while len(d) > 1:
    d.popleft()
    
    if len(d) == 1:
        last = d[0]
        break

    v = d.popleft()
    d.append(v)

print(last)