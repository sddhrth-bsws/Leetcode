# sorted array
nums = [1,1,2,3,4,4,4]
n = len(nums)
j = 1
for i in range(1,n):
    if nums[i] != nums[i-1]:
        nums[j] = nums[i]
        j +=1

print(j,nums)