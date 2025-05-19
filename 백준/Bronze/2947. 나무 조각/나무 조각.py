import sys

nums = list(map(int, sys.stdin.readline().split()))
isChange = False

for i in range(len(nums)):
    for j in range(0, len(nums) - i - 1):
        if nums[j] > nums[j+1]:
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp
            isChange = True
            print(' '.join(map(str, nums)))
    if i == 0 and isChange == False:
        break