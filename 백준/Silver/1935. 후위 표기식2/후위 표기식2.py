import sys
from collections import deque

N = int(sys.stdin.readline())
st = list(sys.stdin.readline().rstrip())
dict = {}
stack = []

for s in st:
    if s.isupper() and s not in dict:
        dict[s] = int(sys.stdin.readline())

for idx, item in enumerate(st):
    if item.isupper() and item in dict:
        st[idx] = dict[item]

d = deque(st)

while d:
    item = d.popleft()
    if isinstance(item, int): #숫자형이면
        stack.append(item)
    elif stack and len(stack) >= 2: #연산자이면
        num2 = stack.pop()
        num1 = stack.pop()
        if item == "*":
            stack.append(num1*num2)
        elif item == "+":
            stack.append(num1+num2)
        elif item == "/":
            stack.append(num1/num2)
        elif item == "-":
            stack.append(num1-num2)

print("{:.2f}".format(stack[0]))
