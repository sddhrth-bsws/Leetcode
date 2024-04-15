def calc():
    nums1 = [4,5,6,0,0,0]
    nums2 = [1,2,3]
    n = len(nums2)
    m = len(nums1)
    act_m = m - n
    # 1st Case
    if(nums2[n-1] <= nums1[0]):
        while(n > 0):
            nums1 = shift(nums1)
            nums1[act_m-1] = nums2[n-1]
            n = n - 1
            act_m = act_m - 1

    print(nums1)

def shift(arr):
    l = len(arr)
    for i in range(l - 1, -1, -1):
        arr[i] = arr[i - 1]

    return arr

calc()