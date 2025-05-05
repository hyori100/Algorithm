import sys
import math
        
N = 123456
array = [0] * 2 + [1] * N * 2

for i in range(2, int(math.sqrt(N*2))+1):
    if array[i] == 1: #남은 수인 경우
        #i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= 2*N:
            array[i*j] = 0
            j += 1

while True:
    M = int(sys.stdin.readline())
    if M == 0:
        break
    print(array[M+1:2*M+1].count(1))