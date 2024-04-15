# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

nums = [2, 7, 11, 15]
target = 9
def twoSum(nums, target):
    numMap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in numMap:
            return [numMap[diff],i]
        numMap[n]=i
    return []
print(twoSum(nums,target))