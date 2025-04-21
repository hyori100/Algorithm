N = int(input())

for i in range(1, N):
    print(" "*(N-i)+"*"+" "*(2*(i-1)-1)+"*"*(0 if i == 1 else 1))

print("*"*(2*N-1))
