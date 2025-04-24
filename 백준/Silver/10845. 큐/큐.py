import sys
from collections import deque

N = int(sys.stdin.readline())
d = deque()

for i in range(0,N):
    s = sys.stdin.readline().split()
    if s[0] == "push":
        d.append(s[1])
    elif s[0] == "pop":
        print(d.popleft() if d else -1)
    elif s[0] == "size":
        print(len(d))
    elif s[0] == "empty":
        print(0 if d else 1)
    elif s[0] == "front":
        print(d[0] if d else -1)
    elif s[0] == "back":
        print(d[-1] if d else -1)