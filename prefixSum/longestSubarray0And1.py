def maxLen(arr):
    # code here
    n = len(arr)
    preSum = 0
    res = 0
    pm = {}
    for i in range(n):
        # for j in range(i,n):
        preSum += -1 if arr[i] == 0 else 1
        if preSum == 0:
            res = i + 1
        if preSum in pm:
            res = max(res, i - pm[preSum])
        else:
            pm[preSum] = i
    print(res)
    return res


def maxLenOld(arr):
    # code here
    n = len(arr)
    preSum = 0
    res = 0
    pm = {}
    for i in range(n):
        # for j in range(i,n):
        preSum += arr[i]
        print(preSum, pm)
        if preSum == 0:
            res = i + 1
        if -preSum in pm:
            res = max(res, i - pm[-preSum])
        else:
            pm[-preSum] = i
    print(res)
    return res


maxLen([1, 0, 1, 1, 1, 0, 0])
maxLenOld([1, 0, 1, 1, 1, 0, 0])
