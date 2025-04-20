import sys

for i in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #" + str(i + 1) + ": " + str(a) + " + " + str(b) + " = " + str(a+b))

