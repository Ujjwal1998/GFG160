def countPairs(arr, target):
    # Your code here
    arr.sort()
    l = 0
    r = len(arr) - 1
    res = 0
    while l < r:
        if arr[l] + arr[r] >= target:
            r -= 1
        else:
            res += r - l
            l += 1
    return res
