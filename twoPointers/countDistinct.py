from collections import defaultdict


def countDistinct(arr, k):
    # Code here
    n = len(arr)
    freq = defaultdict(int)
    res = []
    for i in range(k):
        # window.add(arr[i])
        freq[arr[i]] += 1
    res.append(len(freq))
    for right in range(k, n):
        left = right - k
        if arr[left] in freq:
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                del freq[arr[left]]
        # window.add(arr[right])
        freq[arr[right]] += 1
        # print(window,left)
        res.append(len(freq))
    return res


countDistinct([1, 2, 1, 3, 4, 2, 3], 4)
