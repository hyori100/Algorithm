import sys
        
N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
stk = []
ans = [-1 for i in range(N)]

for i in range(N):
    while stk and arr[stk[-1]] < arr[i]:
        ans[stk[-1]] = arr[i]
        stk.pop(-1)
    stk.append(i)

print(' '.join(map(str, ans)))