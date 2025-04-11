def solution(arr):
    stack = []
    for item in arr:
        if len(stack) == 0 or stack[-1] != item:
            stack.append(item)
    return(stack)