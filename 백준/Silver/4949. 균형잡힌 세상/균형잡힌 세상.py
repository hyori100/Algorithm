while True :
    str = input()
    stack = []

    if str == "." :
        break

    for s in str:
        if s == "(":
            stack.append(")")
        elif s == "[":
            stack.append("]")
        elif s == ")":
            if stack and stack[-1] == ")":
                stack.pop()
            else:
                stack.append(s)
                break
        elif s == "]":
            if stack and stack[-1] == "]":
                stack.pop()
            else:
                stack.append(s)
                break
    if stack:
        print("no")
    else:
        print("yes")