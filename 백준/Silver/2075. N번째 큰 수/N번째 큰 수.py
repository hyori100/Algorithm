import sys
import heapq

N = int(sys.stdin.readline())
hq = []

for _ in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    for a in arr:
        if len(hq) == N:
            heapq.heappushpop(hq, a)
        else:
            heapq.heappush(hq, a)

print(heapq.heappop(hq))