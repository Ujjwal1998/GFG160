def longestSubarraySlow(arr, k):
    n = len(arr)
    res = 0
    for i in range(n):
        csum = 0
        for j in range(i, n):
            csum += arr[j]
            if csum == k:
                res = max(res, j - i + 1)
    print(res)


def longestSubarrayFast(arr, k):
    n = len(arr)
    res = 0
    pre_map = {}
    prefsum = 0
    for i in range(n):
        prefsum += arr[i]
        if prefsum == k:
            res = i + 1
        elif (prefsum - k) in pre_map:
            res = max(res, i - pre_map[prefsum - k])
        if prefsum not in pre_map:
            pre_map[prefsum] = i
    print(res)
    return res


longestSubarraySlow([94, -33, -13, 40, -82, 94, -33, -13, 40, -82], 52)
longestSubarrayFast([94, -33, -13, 40, -82, 94, -33, -13, 40, -82], 52)
