def kthMissing(arr, k):
    # code here
    new_arr = []
    s = set(arr)
    i = 1
    curr = 0
    while curr < k:
        if i not in s:
            curr += 1
            new_arr.append(i)
        i += 1
    # print(new_arr)
    return new_arr[k - 1]


def kthMissingOptimal(arr, k):
    lo = 0
    hi = len(arr) - 1
    res = len(arr) + k

    # Binary Search for index where arr[i] > (i + k)
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] > mid + k:
            res = mid + k
            hi = mid - 1
        else:
            lo = mid + 1

    return res


print(kthMissing([1, 2, 3], k=2))
print(kthMissing([3, 5, 9, 10, 11, 12], k=2))
print(kthMissing([2, 3, 4, 7, 11], k=5))
