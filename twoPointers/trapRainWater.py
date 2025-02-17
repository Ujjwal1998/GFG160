def maxWater(arr):
    # code here
    n = len(arr)
    if n < 3:
        return 0
    final_arr = [0] * n
    for i in range(1, n):
        left_max = 0
        right_max = 0
        for l in range(i):
            left_max = max(arr[l], left_max)
        for r in range(i + 1, n):
            right_max = max(arr[r], right_max)
        # print(arr[i], min(left_max, right_max))
        if arr[i] < min(left_max, right_max):
            final_arr[i] = min(left_max, right_max) - arr[i]
    res = 0
    for j in final_arr:
        res += j
    print(final_arr, res)
    return res


maxWater([1, 2, 3, 4])
