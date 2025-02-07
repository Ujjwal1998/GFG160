def countPairs(arr, target):
    # Complete the function
    l = 0
    r = len(arr) - 1
    res = 0
    while l < r:
        csum = arr[l] + arr[r]
        if csum > target:
            r -= 1
        elif csum < target:
            l += 1
        else:
            elem1 = arr[l]
            cnt1 = 0
            elem2 = arr[r]
            cnt2 = 0
            while (l <= r) and elem1 == arr[l]:
                l += 1
                cnt1 += 1
            while (l <= r) and elem2 == arr[r]:
                r -= 1
                cnt2 += 1
            if elem1 == elem2:
                res += (cnt1 * (cnt1 - 1)) // 2
            else:
                res += cnt1 * cnt2
    return res
