def shift(arr):
    n = len(arr)
    last = arr[n-1]
    for i in range(n-1,-1,-1):
        arr[i] = arr[i-1]
    #arr[1] = last
    return arr

arr = [4,5,6,0,0,0]
print(shift(arr))
print(shift(arr))