def isPrimeNumber(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
    
N = int(input())

s = list(map(int, input().split()))
cnt = 0

for i in s:
    cnt += 1 if isPrimeNumber(i) is True else 0

print(cnt)