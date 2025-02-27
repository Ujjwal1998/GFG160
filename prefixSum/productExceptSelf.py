def productExceptSelf(arr):
    n = len(arr)
    pre_arr = [0] * n
    post_arr = [0] * n
    res = [0] * n
    pre_arr[0] = arr[0]
    post_arr[-1] = arr[-1]
    for i in range(1, n):
        pre_arr[i] = pre_arr[i - 1] * arr[i]
    for i in range(n - 2, -1, -1):
        post_arr[i] = post_arr[i + 1] * arr[i]
    print(pre_arr, post_arr)
    res[0] = post_arr[1]
    res[-1] = pre_arr[-2]
    for i in range(1, n - 1):
        res[i] = pre_arr[i - 1] * post_arr[i + 1]
    print(res)
    return res


productExceptSelf([10, 3, 5, 6, 2])
