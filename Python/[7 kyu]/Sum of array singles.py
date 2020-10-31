def repeats(arr):
    ans = 0
    for i, v in (enumerate(arr, start=0)):
        if arr.count(v) == 1:
            ans+=(arr[i])
    return ans
