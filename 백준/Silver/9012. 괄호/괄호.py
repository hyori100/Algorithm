def checkStr(str):
    stack = []
    for s in str:
        if s == "(":
            stack.append(s)
        elif stack:
            stack.pop()
        else:
            return "NO"
    if stack:
        return "NO"
    else:
        return "YES"

n = int(input())

for _ in range(n):
    str = input()
    print(checkStr(str))