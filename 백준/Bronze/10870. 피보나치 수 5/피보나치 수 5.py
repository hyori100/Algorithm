import sys

N = int(sys.stdin.readline().strip())

def Fibo(num):
    if num == 0 or num == 1:
        return num
    return Fibo(num-2) + Fibo(num-1)

print(Fibo(N))