import sys

N = int(sys.stdin.readline().strip())

arr = []

for i in range(N):
    age, name = sys.stdin.readline().split()
    arr.append((int(age), name, i))
    
arr.sort(key = lambda x: (x[0], x[2]))

for item in arr:
    age, name, _ = item
    print(age, name)