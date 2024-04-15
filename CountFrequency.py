def count_freq(arr,n):
    mp = dict()
    for i in range(n):
        if arr[i] in mp.keys():
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1

    for x in mp:
        print(x, " ", mp[x])
#mp[x] contains the frequencies or in a dict it contains the values
#x in mp contains the keys.
arr = [1,1,2,3,4,4,4]
n = len(arr)

count_freq(arr,n)