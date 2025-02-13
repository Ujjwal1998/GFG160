def longestUniqueSubstrNaive(s):
    n = len(s)
    res = 0
    for i in range(n):
        visited = [False] * 26
        for j in range(i, n):
            current = ord(s[j]) - ord("a")
            # print(current, s[j])
            if visited[current]:
                break
            visited[current] = True
            res = max(res, j - i + 1)
    print(res)


def longestUniqueSubstrFast(s):
    # code here
    n = len(s)
    if n == 1:
        return 1
    start, end = 0, 0
    res = 0
    window = set()
    # for i in range(n):
    while end < n:
        print(end, s)
        # if s[end] not in window:
        #     window.add(s[end])
        #     res = max(res, end - start + 1)
        # else:
        #     start += 1
        while s[end] in window:
            window.remove(s[start])
            start += 1
        window.add(s[end])
        res = max(res, end - start + 1)
        end += 1

    print(res)


#         return res
longestUniqueSubstrNaive("geeksforgeeks")
longestUniqueSubstrFast("hqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvs")
