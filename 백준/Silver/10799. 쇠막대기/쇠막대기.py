import sys

itemList = sys.stdin.readline()
stack = []
answer = 0

for idx, item in enumerate(itemList):
    if itemList[idx] == "(":
        stack.append("(")
    elif stack:
        stack.pop()
        if itemList[idx-1] == "(":
            answer += len(stack)
        else:
            answer += 1

print(answer)