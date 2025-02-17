def maxWater(arr):
    n = len(arr)
    if n == 1:
        return 0
    l = 0
    r = n - 1
    res = 0
    while l < r:
        base = r - l
        height = min(arr[l], arr[r])
        res = max(res, base * height)
        if arr[l] < arr[r]:
            l += 1
        else:
            r -= 1
    return res
