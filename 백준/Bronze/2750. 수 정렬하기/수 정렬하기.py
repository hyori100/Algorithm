import sys

N = int(input())

arr = [int(sys.stdin.readline().strip()) for i in range(N)]
arr.sort()

for a in arr:
    print(a)