import sys

strd = list(sys.stdin.readline().strip())

strd.sort(reverse=True)

print(''.join(strd))