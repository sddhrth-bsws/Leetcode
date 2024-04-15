def calc():
    nums1 = [4, 5, 6,0,0,0]
    nums2 = [1,2,3]
    i = 0
    m = len(nums1)
    n = len(nums2)
    act_m = m - n
    k = n-1
    j = m-1
    first = nums1[0]
    while(act_m>-1):
        if( k == -1):
            break
        else:
            if(nums2[k]>=nums1[act_m-1]):
                nums1[j] = nums2[k]
                k = k-1
                j = j-1

            else:
                nums1 = shift_right(act_m-1,nums1)
                act_m = act_m - 1
                j = j - 1
                '''
                if(act_m == 0):
                    nums1[0] = nums2[k]
                    #break
                else:
                    nums1[act_m] = nums1[act_m-1]
                    act_m = act_m - 1
                    j = j -1
                '''

    print(nums1)

def shift_right(index,arr):
    l = len(arr)
    last = arr[l-1]
    for i in range(l-1,index,-1):
        arr[i]=arr[i-1]
    #arr[index] = last
    #print(arr)
    return arr


calc()
