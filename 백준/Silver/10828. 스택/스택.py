import sys

N = int(sys.stdin.readline())
stack = []
cnt = 0

for _ in range(N):
    s = sys.stdin.readline().split()
    if s[0] == "push":
        num = int(s[1])
        stack.append(num)
        cnt += 1
    elif s[0] == "pop":
        if stack:
            num = stack.pop()
            cnt -= 1
            print(num)
        else:
            print(-1)
    elif s[0] == "size":
        print(cnt)
    elif s[0] == "empty":
        print(0 if stack else 1)
    elif s[0] == "top":
        print(stack[-1] if stack else -1)
