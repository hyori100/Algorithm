from collections import deque
import sys

N = int(sys.stdin.readline())
d = deque()

for _ in range(N):
    s = sys.stdin.readline().split()
    if s[0] == "push":
        d.append(int(s[1]))
    elif s[0] == "pop":
        if d:
          num = d.popleft()
          print(num)
        else:
            print(-1)
    elif s[0] == "size":
        print(len(d))
    elif s[0] == "empty":
        if d:
            print(0)
        else:
            print(1)
    elif s[0] == "front":
        if d:
            print(d[0])
        else:
            print(-1)
    elif s[0] == "back":
        if d:
            print(d[-1])
        else:
            print(-1)
