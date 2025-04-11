def solution(s):
    stack = []
    for item in s:
        if item == "(":
            stack.append(item)
        elif not stack:
            return False
        elif stack[-1] == item:
            return False
        else:
            stack.pop()
    if stack:
        return False
    return True