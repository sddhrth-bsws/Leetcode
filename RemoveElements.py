def calc(nums,val):
    n = len(nums)
    j = 0
    i = 0
    for i in range(n):
        if nums[i] != val:
            nums[j] = nums[i]
            j = j+1

    return nums

def input():
    arr1 = [0, 1, 2, 2, 3, 0, 4, 2]
    print(calc(arr1,3))
    arr2 = [0,1,2,2,3]
    print(calc(arr2,2))

input()