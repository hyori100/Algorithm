import sys

coinNum, sumNum = map(int, sys.stdin.readline().split())
coins = []

for i in range(coinNum):
    num = int(input())
    if sumNum >= num:
        coins.append(num)
coins.sort(reverse=True)

curLeft = sumNum
ans = 0

curLeft = sumNum
for coin in coins:
    if coin > curLeft:
        continue
    s = curLeft // coin
    if s >= 1:
        curLeft = curLeft - s * coin
        ans += s
print(ans)
