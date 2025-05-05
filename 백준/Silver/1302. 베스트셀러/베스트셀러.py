import sys
from collections import Counter

booksLen = int(sys.stdin.readline())

books = [input() for i in range(booksLen)]
booksCounter = Counter(books)

maxCnt = max(booksCounter.values())
ans = []

for k,v in booksCounter.items():
    if v == maxCnt:
        ans.append(k)

ans.sort()
print(ans[0])