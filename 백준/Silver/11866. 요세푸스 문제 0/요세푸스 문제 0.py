from collections import deque

a,b = input().split()

d = deque()
seq = int(b)
answer = []

for i in range(1, int(a)+1):
    d.append(i)

while d:
    for i in range(seq):
        num = d.popleft()
        if i + 1 == seq:
            answer.append(str(num))
        else:
            d.append(num)

print('<'+', '.join(answer)+'>')