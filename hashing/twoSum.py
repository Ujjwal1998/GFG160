def twoSum(arr, target):
    map = {}
    n = len(arr)
    for i in range(n):
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1
    for i in range(n):
        c = target - arr[i]
        map[arr[i]] -= 1
        if c in map and map[c] > 0:
            return True
