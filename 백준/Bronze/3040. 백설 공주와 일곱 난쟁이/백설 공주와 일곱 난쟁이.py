from itertools import combinations

arr = [int(input()) for _ in range(9)]

for i in combinations(arr,7):
    if sum(i) == 100:
        for num in i:
            print(num)
        break