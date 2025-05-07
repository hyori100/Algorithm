from itertools import permutations

arr = [int(input()) for _ in range(9)]

for i in permutations(arr,7):
    if sum(i) == 100:
        for num in i:
            print(num)
        break