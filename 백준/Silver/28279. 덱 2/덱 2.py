from collections import deque
import sys

N = int(sys.stdin.readline())
d = deque()

for _ in range(N):
    s = sys.stdin.readline().split()
    if s[0] == "1":
        d.appendleft(int(s[1]))
    elif s[0] == "2":
        d.append(int(s[1]))
    elif s[0] == "3":
        if d:
            v = d.popleft()
            print(v)
        else:
            print(-1)
    elif s[0] == "4":
        if d:
            v = d.pop()
            print(v)
        else:
            print(-1)
    elif s[0] == "5":
        print(len(d))
    elif s[0] == "6":
        if d:
            print(0)
        else:
            print(1)
    elif s[0] == "7":
        if d:
            print(d[0])
        else:
            print(-1)
    elif s[0] == "8":
        if d:
            print(d[-1])
        else:
            print(-1)