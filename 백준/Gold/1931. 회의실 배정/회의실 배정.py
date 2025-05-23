import sys

N = int(sys.stdin.readline())
meetings = []

for i in range(N):
    start,end = map(int, input().split())
    meetings.append((end, start))
meetings.sort()

t = 0
ans = 0

for end, start in meetings:
    if t <= start:
        ans += 1
        t = end
print(ans)