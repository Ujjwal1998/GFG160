def subarraySum(arr, target):
    # code here
    n = len(arr)
    s, e = 0, 0
    csum = 0
    for i in range(n):
        csum += arr[i]
        if csum >= target:
            e = i
            while csum > target and s < e:
                csum -= arr[s]
                s += 1
            if csum == target:
                return [s + 1, e + 1]
    return [-1]
