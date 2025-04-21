import sys

N = sys.stdin.readline()

numList = list(map(int, sys.stdin.readline().split()))
print(min(numList), max(numList))
