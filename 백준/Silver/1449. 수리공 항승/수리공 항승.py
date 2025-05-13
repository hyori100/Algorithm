import sys

holeNum, tapeLen = map(int, sys.stdin.readline().split())

arr = [False] * 1001

for i in map(int, input().split()):
    arr[i] = True

x = 0
ans = 0

while x <= 1000:
    if arr[x]:
        x += tapeLen
        ans += 1
    else:
        x += 1

print(ans)