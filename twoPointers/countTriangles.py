def countTriangles(arr):
    # code here
    arr.sort()
    n = len(arr)
    res = 0
    for third in range(2, n):
        first = 0
        second = third - 1
        while first < second:
            if arr[first] + arr[second] > arr[third]:
                res += second - first
                second -= 1
            else:
                first += 1
    return res
