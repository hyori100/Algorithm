import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    s = sys.stdin.readline().split()
    if s[0] == "1":
        stack.append(int(s[1]))
    elif s[0] == "2":
        if stack:
            v = stack.pop()
            print(v)
        else:
            print(-1)
    elif s[0] == "3":
        print(len(stack))
    elif s[0] == "4":
        if stack:
            print(0)
        else:
            print(1)
    elif s[0] == "5":
        if stack:
            print(stack[-1])
        else:
            print(-1)
