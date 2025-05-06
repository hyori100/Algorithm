import sys
from collections import deque

N = int(sys.stdin.readline())
stack = []
stack2 = []

for _ in range(N):
    stack = []
    stack2 = []
    case = sys.stdin.readline().strip()
    for word in case:
        if word == "<" and stack:
            stack2.append(stack.pop())
        elif word == ">" and stack2:
            stack.append(stack2.pop())
        elif word == "-" and stack:
            stack.pop()
        elif word != "<" and word != ">" and word != "-":
            stack.append(word)
        #while stack2:
          #  stack.append(stack2.pop())
    print(''.join(stack)+''.join(reversed(stack2)))
