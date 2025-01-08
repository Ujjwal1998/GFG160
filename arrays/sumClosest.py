def sumClosestSlow(arr, target):
    # code here
    candidates = set()
    min_val = float("inf")
    n = len(arr)
    if n == 1:
        return []
    for i in range(n):
        for j in range(i + 1, n):
            first = min(arr[i], arr[j])
            second = max(arr[i], arr[j])
            curr_sum = arr[i] + arr[j]
            diff = abs(curr_sum - target)
            if diff < min_val:
                min_val = diff
                candidates.clear()
                candidates.add((first, second))
            if diff == min_val:
                current = candidates.pop()
                if abs(current[0] - current[1]) < abs(first - second):
                    candidates.add((first, second))
                else:
                    candidates.add(current)
    return candidates.pop()


def sumClosestFast(arr, target):
    candidates = set()
    min_val = float("inf")
    n = len(arr)
    if n == 1:
        return []
    arr.sort()
    lo = 0
    hi = n - 1
    while lo < hi:
        curr_sum = arr[lo] + arr[hi]
        diff = abs(curr_sum - target)
        if diff < min_val:
            min_val = diff
            candidates.clear()
            candidates.add((arr[lo], arr[hi]))
        if diff == min_val:
            current = candidates.pop()
            if abs(current[0] - current[1]) < abs(arr[lo] - arr[hi]):
                candidates.add((arr[lo], arr[hi]))
            else:
                candidates.add(current)
        if curr_sum > target:
            hi = hi - 1
        elif curr_sum < target:
            lo = lo + 1
        else:
            return (arr[lo], arr[hi])

    return candidates.pop()


print(sumClosestFast([10, 30, 20, 5], 25))
print(sumClosestFast([5, 2, 7, 1, 4], 10))
print(sumClosestFast([10, 10], 10))
