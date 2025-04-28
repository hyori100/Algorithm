import sys
        
left = list(sys.stdin.readline().rstrip())
right = []


N = int(sys.stdin.readline())

for i in range(N):
    m = sys.stdin.readline().split()
    if m[0] == "L" and left:
        right.append(left.pop())
    elif m[0] == "D" and right:
        left.append(right.pop())
    elif m[0] == "B" and left:
        left.pop()
    elif m[0] == "P":
        left.append(m[1])

answer = left + right[::-1]
print(''.join(answer))
