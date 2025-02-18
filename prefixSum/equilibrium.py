def findEquilibrium(arr):
    # code here
    n = len(arr)
    pre_arr = [0] * n
    suff_arr = [0] * n
    pre_arr[0] = arr[0]
    suff_arr[n - 1] = arr[n - 1]
    for i in range(1, n):
        pre_arr[i] = pre_arr[i - 1] + arr[i]
    for i in range(n - 2, -1, -1):
        suff_arr[i] = suff_arr[i + 1] + arr[i]
    for i in range(len(pre_arr)):
        if pre_arr[i] == suff_arr[i]:
            return i
    return -1


print(findEquilibrium([1, 2, 0, 3]))
