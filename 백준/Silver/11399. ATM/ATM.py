import sys

N = int(input())

times = list(map(int, sys.stdin.readline().split()))
times.sort()

cursum = 0
ans = 0

for t in times:
    cursum += t
    ans += cursum

print(ans)
