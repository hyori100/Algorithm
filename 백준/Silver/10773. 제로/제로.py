n = int(input())
inputs = []
stack = []
for _ in range(n):
    inputs.append(int(input()))

for item in inputs:
    if item != 0:
        stack.append(item)
    else:
        stack.pop()

print(sum(stack))