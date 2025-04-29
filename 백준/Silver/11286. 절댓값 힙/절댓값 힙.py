import sys
import heapq
        
N = int(sys.stdin.readline())
heap = []

for i in range(N):
    M = int(sys.stdin.readline())
    if M == 0:
        print(heapq.heappop(heap)[1] if heap else 0)
    else:
        heapq.heappush(heap, (abs(M), M))